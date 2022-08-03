import json
from pathlib import Path

from django.utils.translation import gettext_lazy as _

from project.env import env

# Project root

BASE_DIR = Path(__file__).resolve().parent.parent


# Core settings

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

SERVICE_CLIENT_URL = env('SERVICE_CLIENT_URL')

SERVICE_SITE_URL = env('SERVICE_SITE_URL')


# Application definition

LOCAL_APPS = [
    'project.api',
    'project.db',
    'project.user',
]

THIRDPARTY_APPS = [
    'corsheaders',
    'django_filters',
    'django_hosts',
    'django_ses',
    'rest_framework',
    'storages',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # django site
    'django.contrib.sitemaps',  # django sitemap
    *THIRDPARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',  # django gzip
    'django_hosts.middleware.HostsRequestMiddleware',  # django hosts
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # django locale
    'corsheaders.middleware.CorsMiddleware',  # django cors header
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',  # django hosts
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database

if env('DATABASE_URL'):
    DATABASES = {'default': env.db('DATABASE_URL')}

    if env('READONLY_DATABASE_URL'):
        DATABASES['readonly'] = env.db('READONLY_DATABASE_URL')
        DATABASE_ROUTERS = ['project.routers.ReadOnlyRouter']


# Password validation

default_validation_prefix = 'django.contrib.auth.password_validation.'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{default_validation_prefix}UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{default_validation_prefix}MinimumLengthValidator',
    },
    {
        'NAME': f'{default_validation_prefix}CommonPasswordValidator',
    },
    {
        'NAME': f'{default_validation_prefix}NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = env('LANGUAGE_CODE')

TIME_ZONE = env('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Locale

LANGUAGES = [('en', _('English'))]

LOCALE_PATHS = [BASE_DIR / 'locale']


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = 'static/'

STATIC_URL = '/static/'


# Media files

MEDIA_ROOT = 'media/'

MEDIA_URL = '/media/'


# AWS Storage backends

AWS_S3_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')

AWS_S3_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

AWS_S3_REGION = env('AWS_S3_REGION')

AWS_S3_BUCKET = env('AWS_S3_BUCKET')

AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')

AWS_S3_MEDIA_LOCATION = env('AWS_S3_MEDIA_LOCATION')

AWS_S3_STATIC_LOCATION = env('AWS_S3_STATIC_LOCATION')

if AWS_S3_BUCKET:
    DEFAULT_FILE_STORAGE = 'project.storages.MediaStorage'
    STATICFILES_STORAGE = 'project.storages.StaticStorage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}{AWS_S3_MEDIA_LOCATION}'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}{AWS_S3_STATIC_LOCATION}'


# Django Hosts

DEFAULT_HOST = 'admin'

ROOT_HOSTCONF = 'project.hosts'


# Django CORS headers

CORS_ALLOW_ALL_ORIGINS = DEBUG

CORS_ALLOWED_ORIGINS = [SERVICE_CLIENT_URL]


# HTTPS

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# CSRF

CSRF_TRUSTED_ORIGINS = [SERVICE_SITE_URL]


# Django rest framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'project.api.authentication.CognitoAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/minute',
        'user': '200/minute',
    },
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': (
        'rest_framework.negotiation.DefaultContentNegotiation'
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
    'EXCEPTION_HANDLER': 'project.api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'project.api.pagination.CursorPagination',
    'PAGE_SIZE': env('API_DEFAULT_PAGE_SIZE'),
}


# django ses

AWS_SES_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')

AWS_SES_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

AWS_SES_REGION_NAME = env('AWS_SES_REGION')

AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'

DEFAULT_FROM_EMAIL = env('DEFAULT_EMAIL')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEFAULT_FROM_EMAIL:
    EMAIL_BACKEND = 'django_ses.SESBackend'


# Amazon Cognito

AWS_COGNITO_REGION = env('AWS_COGNITO_REGION')

AWS_COGNITO_DOMAIN = f'cognito-idp.{AWS_COGNITO_REGION}.amazonaws.com'

AWS_COGNITO_POOL_ID = env('AWS_COGNITO_POOL_ID')

AWS_COGNITO_ENDPOINT = f'https://{AWS_COGNITO_DOMAIN}/{AWS_COGNITO_POOL_ID}'

AWS_COGNITO_CLIENT_ID = env('AWS_COGNITO_CLIENT_ID')

with open('jwks.json', 'r', encoding='utf-8') as f:
    AWS_COGNITO_JWKS = json.load(f)


# django site

SITE_ID = 1


# custom user

# AUTH_USER_MODEL = ''
