import json
import boto3
import uuid
from botocore.config import Config

BUCKET_NAME = "my-image-upload-2026-yash"

s3 = boto3.client(
    "s3",
    region_name="ap-south-1",
    config=Config(
        signature_version="s3v4",
        s3={
            "addressing_style": "virtual"
        }
    )
)


def lambda_handler(event, context):

    file_name = f"uploads/{uuid.uuid4()}"

    upload_url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": file_name
        },
        ExpiresIn=300
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "upload_url": upload_url,
            "file_key": file_name
        })
    }
