import json

def lambda_handler(event, context):
    # Get the bucket name and key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Print the event details
    print(f"Received event from bucket: {bucket_name}, key: {object_key}")

    # Return a simple response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda')
    }
