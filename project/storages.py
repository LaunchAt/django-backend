from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket_name'] = settings.AWS_S3_BUCKET
        kwargs['custom_domain'] = settings.AWS_S3_CUSTOM_DOMAIN
        kwargs['location'] = settings.AWS_S3_MEDIA_LOCATION
        super(MediaStorage, self).__init__(*args, **kwargs)


class StaticStorage(S3Boto3Storage):
    def __init__(self, *args, **kwargs):
        kwargs['bucket_name'] = settings.AWS_S3_BUCKET
        kwargs['custom_domain'] = settings.AWS_S3_CUSTOM_DOMAIN
        kwargs['location'] = settings.AWS_S3_STATIC_LOCATION
        super(StaticStorage, self).__init__(*args, **kwargs)
