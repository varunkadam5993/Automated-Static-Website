import boto3
import os
import mimetypes
from botocore.exceptions import ClientError

# ==============================
# Configuration
# ==============================

BUCKET_NAME = "my-static-website-2026-demo32"
REGION = "ap-south-1"

# Use the folder where deploy.py is located
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

s3 = boto3.client("s3", region_name=REGION)


# ==============================
# Create S3 Bucket
# ==============================

def create_bucket():

    try:
        s3.head_bucket(Bucket=BUCKET_NAME)

        print(f"Bucket already exists: {BUCKET_NAME}")

    except ClientError:

        print(f"Creating bucket: {BUCKET_NAME}")

        if REGION == "us-east-1":

            s3.create_bucket(
                Bucket=BUCKET_NAME
            )

        else:

            s3.create_bucket(
                Bucket=BUCKET_NAME,
                CreateBucketConfiguration={
                    "LocationConstraint": REGION
                }
            )

        print("Bucket created successfully.")


# ==============================
# Configure Static Website
# ==============================

def configure_website():

    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            "IndexDocument": {
                "Suffix": "index.html"
            },
            "ErrorDocument": {
                "Key": "error.html"
            }
        }
    )

    print("Static website hosting configured.")


# ==============================
# Upload Website Files
# ==============================

def upload_files():

    # Files/folders that should NOT be uploaded
    exclude_files = {
        "deploy.py"
    }

    exclude_folders = {
        ".git",
        "__pycache__",
        ".idea",
        ".vscode"
    }

    for root, directories, files in os.walk(PROJECT_FOLDER):

        # Remove excluded folders
        directories[:] = [
            directory
            for directory in directories
            if directory not in exclude_folders
        ]

        for file in files:

            # Skip Python deployment script
            if file in exclude_files:
                continue

            local_path = os.path.join(root, file)

            # Create S3 key relative to project folder
            s3_key = os.path.relpath(
                local_path,
                PROJECT_FOLDER
            ).replace("\\", "/")

            # Detect content type
            content_type, _ = mimetypes.guess_type(
                local_path
            )

            if content_type is None:
                content_type = "application/octet-stream"

            print(f"Uploading: {s3_key}")

            s3.upload_file(
                local_path,
                BUCKET_NAME,
                s3_key,
                ExtraArgs={
                    "ContentType": content_type
                }
            )

    print("\nAll website files uploaded successfully.")


# ==============================
# Display Website URL
# ==============================

def display_website_url():

    website_url = (
        f"http://{BUCKET_NAME}.s3-website-"
        f"{REGION}.amazonaws.com"
    )

    print("\n====================================")
    print("Website Deployment Successful!")
    print("====================================")

    print(f"Bucket: {BUCKET_NAME}")
    print(f"Region: {REGION}")
    print(f"Website URL: {website_url}")

    print("\nOpen the above URL in your browser.")


# ==============================
# Main Function
# ==============================

if __name__ == "__main__":

    print("\nStarting website deployment...\n")

    create_bucket()

    configure_website()

    upload_files()

    display_website_url()
