from pathlib import Path

import environ

env = environ.Env(
    DATABASE_URL=(str, 'sqlite:///db.sqlite3'),
    DEBUG=(bool, False),
    LANGUAGE_CODE=(str, 'en-us'),
    READONLY_DATABASE_URL=(str, ''),
    SECRET_KEY=(str, ''),
    SERVICE_CLIENT_URL=(str, 'http://localhost'),
    SERVICE_SITE_URL=(str, 'http://localhost'),
    TIME_ZONE=(str, 'UTC'),
    AWS_ACCESS_KEY_ID=(str, ''),
    AWS_SECRET_ACCESS_KEY=(str, ''),
    AWS_S3_BUCKET=(str, ''),
    AWS_S3_CUSTOM_DOMAIN=(str, ''),
    AWS_S3_MEDIA_LOCATION=(str, '/media/'),
    AWS_S3_STATIC_LOCATION=(str, '/static/'),
    AWS_S3_REGION=(str, 'us-east-1'),
    AWS_SES_REGION=(str, 'us-east-1'),
    DEFAULT_EMAIL=(str, ''),
    AWS_COGNITO_REGION=(str, 'us-east-1'),
    AWS_COGNITO_POOL_ID=(str, ''),
    AWS_COGNITO_CLIENT_ID=(str, ''),
    API_DEFAULT_PAGE_SIZE=(int, 10),
)

ENV_PATH = Path(__file__).resolve().parent.parent / '.env'

environ.Env.read_env(ENV_PATH)
