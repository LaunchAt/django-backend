from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, status, views


class UserAccountDeleted(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Your account has already archived.')
    default_code = 'account_deleted'


class UserAccountFrozen(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Your account is frozen.')
    default_code = 'account_frozen'


class UserAccountNotVerified(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Your account is not verified.')
    default_code = 'account_not_verified'


def exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = views.exception_handler(exc, context)

    if response:
        if type(response.data) is list:
            response.data = {'detail': response.data[0]}

        response.data.update(
            {
                'code': response.default_code,
                'message': response.default_detail,
            }
        )

    return response
