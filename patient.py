import json
import boto3

   
    
def listPatients(event, context):
   
    s3 = boto3.client('s3')
    bucket_name = "mypatient"
    file_name = "patient.json"
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    json_data = json.loads(response['Body'].read())
    print(json_data)
   
   
    return {
        "statusCode": 200,
        "body": json.dumps(json_data)
    }
