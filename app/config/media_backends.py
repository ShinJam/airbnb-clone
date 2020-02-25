import os

from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    # bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    location = 'uploads'
    file_overwrite = False