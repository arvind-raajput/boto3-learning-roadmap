import boto3


def create_bucket(bucket_name, region="us-east-1"):
    try:
        if region == "us-east-1":
            s3_client = boto3.client("s3", region_name=region)
            response = s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client("s3", region_name=region)
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket {bucket_name} created successfully")
        return response
    except Exception as e:
        print(f"Error - {e}")
if __name__ == "__main__":
    create_bucket("akrlabs-19198125")
