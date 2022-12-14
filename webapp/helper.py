import boto3

def upload_image(file_name, bucket, object_name):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name.filename
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response