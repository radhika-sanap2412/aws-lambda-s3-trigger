# AWS Lambda S3 Bucket Listing Tutorial

This tutorial guides you through the process of creating an AWS Lambda function that lists all your S3 buckets.

## Prerequisites

- AWS Account
- Basic knowledge of AWS Lambda and S3
- AWS CLI installed and configured
- Access to AWS Management Console

## Steps

### 1. Create an S3 Bucket

Create an S3 bucket that will be used in this tutorial.

![S3 Buckets Display](.listing_bucket_names_using_lambda/s3_buckets_display.jpg)

### 2. Create a Lambda Function

- Go to AWS Lambda in the AWS Management Console.
- Click on "Create function."
- Choose "Author from scratch."
- Fill in the function name and choose Python 3.12 as the runtime.
- Under "Permissions," choose "Create a new role with basic Lambda permissions."

![Create Lambda Function](./create_lambda_function.jpg)

### 3. Set Lambda Function Code

- After the Lambda function is created, set up the code for the function.

```python
import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket_list = [] 
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket_list.append(bucket.name)
    return {
        'StatusCode': 200,
        'body': bucket_list
    }
