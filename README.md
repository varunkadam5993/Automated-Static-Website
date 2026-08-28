# Automated-Static-Website
# AWS S3 Static Website Hosting

A simple static website hosted on **Amazon Web Services (AWS)** using **Amazon S3 Static Website Hosting**.

The main purpose of this project is to learn how to deploy a website to the cloud using AWS S3 and automate the deployment process with Python and Boto3.

---

## 🚀 Project Overview

In this project, I created a static website called **Sahyadri Trekkers**, which provides information about trekking and historical forts in Maharashtra.

The website is hosted on **Amazon S3**.

Instead of manually uploading website files to S3, I created a Python script using **Boto3** that can:

* Create an S3 bucket
* Configure static website hosting
* Upload website files
* Detect file content types
* Display the S3 website URL

### AWS Services Used

* **Amazon S3** – Static website hosting
* **AWS IAM** – Permissions and access control
* **Boto3** – Python SDK for AWS

---

## ☁️ AWS Architecture

```text
             Website Files
          ┌─────────────────┐
          │   index.html    │    
          │   Other Files   │
          └────────┬────────┘
                   │
                   │ Python + Boto3
                   ▼
          ┌─────────────────┐
          │   Amazon S3     │
          │                 │
          │  S3 Bucket      │
          │                 │
          │ Static Website  │
          │    Hosting      │
          └────────┬────────┘
                   │
                   │ HTTP
                   ▼
              🌐 Internet
                   │
                   ▼
               User Browser
```

---

## 🛠️ Technologies

| Technology | Purpose               |
| ---------- | --------------------- |
| HTML5      | Website               |
| CSS3       | Styling               |
| JavaScript | Website interaction   |
| Python     | Deployment automation |
| Boto3      | AWS SDK               |
| Amazon S3  | Website hosting       |
| AWS IAM    | Permissions           |

---

## 📁 Project Structure

```text
aws-static-website/
│
├── index.html
├── deploy.py
├── README.md
└── .gitignore
```

---

## ⚙️ AWS Configuration

The project uses the following S3 configuration:

```python
BUCKET_NAME = "my-static-website-2026-demo32"
REGION = "ap-south-1"
```

The region is:

**Asia Pacific (Mumbai) – `ap-south-1`**

---

## 🔐 AWS IAM

AWS credentials are required to allow the Python script to communicate with Amazon S3.

The deployment user needs appropriate S3 permissions such as:

```text
s3:HeadBucket
s3:CreateBucket
s3:PutBucketWebsite
s3:PutObject
s3:PutBucketPolicy
```

For security, AWS credentials should **not** be written directly inside the Python source code.

AWS CLI can be configured using:

```bash
aws configure
```

---

## 📦 Install Boto3

Install the AWS SDK for Python:

```bash
pip install boto3
```

Verify Python:

```bash
python --version
```

---

## ▶️ Deploy Website

Run the deployment script:

```bash
python deploy.py
```

The script performs the following steps:

```text
1. Check S3 Bucket
        ↓
2. Create Bucket if required
        ↓
3. Configure Static Website Hosting
        ↓
4. Find Website Files
        ↓
5. Upload Files to S3
        ↓
6. Display Website URL
```

---

## 🪣 S3 Bucket Creation

The Python script checks whether the bucket already exists.

If it does not exist, it creates the bucket in:

```text
ap-south-1
```

The code uses Boto3:

```python
s3.create_bucket(
    Bucket=BUCKET_NAME,
    CreateBucketConfiguration={
        "LocationConstraint": REGION
    }
)
```

---

## 🌐 Static Website Hosting

The project uses Amazon S3 Static Website Hosting.

The deployment script configures:

```text
Index Document → index.html
Error Document → error.html
```

Using:

```python
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
```

---

## 📤 Uploading Website Files

The Python script automatically searches the project folder and uploads the website files to S3.

It excludes unnecessary files and folders such as:

```text
.git
__pycache__
.idea
.vscode
deploy.py
```

This keeps the S3 bucket focused on website files.

---

## 📄 Content-Type Detection

The deployment script automatically detects the MIME type of files before uploading them.

For example:

```text
HTML → text/html
CSS  → text/css
JS   → text/javascript
PNG  → image/png
JPG  → image/jpeg
```

This helps browsers correctly interpret the uploaded files.

---

## 🔓 S3 Public Access

Because this project uses the traditional **S3 Static Website Hosting endpoint**, the website objects need to be publicly readable.

A public bucket policy can be used to allow:

```text
s3:GetObject
```

for website objects.

Example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-static-website-2026-demo32/*"
    }
  ]
}
```

### Important

S3 **Block Public Access** settings can prevent a public bucket policy from being saved.

If public static website hosting is intentional, the relevant bucket-level public access settings must be configured appropriately.

> ⚠️ Public S3 access should only be enabled when you intentionally want the website and its objects to be publicly accessible.

---

## 🌍 Website URL

After deployment, the Python script displays the S3 website endpoint.

For this project:

```text
http://my-static-website-2026-demo32.s3-website-ap-south-1.amazonaws.com
```

The URL is generated by the deployment script.

---

## 🎯 Main AWS Learning

This project helped me understand the basic process of hosting a website on AWS:

```text
Local Website
      ↓
Amazon S3 Bucket
      ↓
Static Website Hosting
      ↓
Bucket Policy
      ↓
Public Access
      ↓
S3 Website Endpoint
      ↓
Internet 🌐
```

I also learned how to automate AWS operations using **Python and Boto3** instead of performing every step manually through the AWS Console.

---

## 📚 AWS Concepts Learned

Through this project, I learned:

* Amazon S3 buckets
* S3 objects
* S3 Static Website Hosting
* S3 website endpoints
* S3 bucket policies
* S3 Block Public Access
* AWS IAM permissions
* AWS regions
* Boto3
* Automated file uploads
* MIME/content types
* Basic cloud deployment

---

## 🔮 Future Improvements

The project can be improved by adding:

* **Amazon CloudFront** for CDN and HTTPS
* **AWS Certificate Manager** for SSL/TLS
* **Amazon Route 53** for a custom domain
* **AWS Lambda** for backend functionality
* **API Gateway** for APIs
* **Amazon DynamoDB** for storing booking information
* **Amazon SNS/SES** for notifications and emails
* **GitHub Actions** for CI/CD deployment

A future architecture could be:

```text
User
  ↓
Route 53
  ↓
CloudFront
  ↓
S3
  ↓
Static Website
```

---

## 👨‍💻 Author

**Varun Kadam**


---

## 📌 Project Goal

> **The main goal of this project is to understand how a static website can be hosted and deployed on AWS using Amazon S3, with deployment automated using Python and Boto3.**
