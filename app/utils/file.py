from minio import Minio
import os
from datetime import timedelta

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
BUCKET_NAME = os.environ.get("MINIO_BUCKET")

client = Minio("play.min.io", ACCESS_KEY, SECRET_KEY)


def upload_to_minio(filename: str, data, length: int):
    # Make bucket if not exist.
    found = client.bucket_exists(BUCKET_NAME)
    if not found:
        client.make_bucket(BUCKET_NAME)

    client.put_object(BUCKET_NAME, filename, data, length)


def get_path(filename: str, expires: int):
    expiration_time = timedelta(days=expires)
    return client.presigned_get_object(BUCKET_NAME, filename, expires=expiration_time)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
