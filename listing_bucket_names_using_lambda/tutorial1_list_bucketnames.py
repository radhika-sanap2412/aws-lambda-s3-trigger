import json  # Importing the JSON module for formatting responses
import boto3  # Importing the Boto3 library to interact with AWS services

# Create an S3 resource object to interact with the S3 service
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    """
    AWS Lambda handler function that lists all S3 buckets.
    
    :param event: The event data passed to the function when invoked.
    :param context: The context object provides runtime information to the handler.
    :return: JSON object containing the status code and the list of bucket names.
    """
    
    # Initialize an empty list to store bucket names
    bucket_list = [] 
    
    # Iterate over all the buckets in the S3 account
    for bucket in s3.buckets.all():
        print(bucket.name)  # Print each bucket name to CloudWatch logs
        
        # Append the bucket name to the bucket_list
        bucket_list.append(bucket.name)
        
        # Return the response with status code and the list of bucket names
        # Note: The 'return' statement should be outside of the 'for' loop to capture all buckets
        return {
            'StatusCode': 200,  # HTTP status code indicating successful execution
            'body': bucket_list  # The list of bucket names as the response body
        }
