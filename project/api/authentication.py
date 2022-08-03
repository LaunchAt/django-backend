import json

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication

from project.api.exceptions import (
    UserAccountDeleted,
    UserAccountFrozen,
    UserAccountNotVerified,
)

cognito_issuer = settings.AWS_COGNITO_ENDPOINT
cognito_audience = settings.AWS_COGNITO_CLIENT_ID
cognito_jwks = settings.AWS_COGNITO_JWKS


class CognitoAuthentication(TokenAuthentication):
    keyword = 'JWT'
    model = get_user_model()

    def get_data(self, token):
        headers = jwt.get_unverified_header(token)
        jwks = {key['kid']: json.dumps(key) for key in cognito_jwks['keys']}
        jwk = jwks.get(headers['kid'])
        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(jwk)

        return jwt.decode(
            token,
            public_key,
            audience=cognito_audience,
            issuer=cognito_issuer,
            algorithms=['RS256'],
        )

    def authenticate_credentials(self, key):
        model = self.get_model()
        data = self.get_data(key)
        is_verified = data.get('email_verified')

        if not is_verified:
            raise UserAccountNotVerified()

        user, _ = model.objects.get_or_create(
            id=data.get('cognito:username'),
            email=data.get('email'),
            username=data.get('preferred_username'),
        )

        if user.is_deleted:
            raise UserAccountDeleted()

        if user.is_frozen:
            raise UserAccountFrozen()

        return (user, None)
