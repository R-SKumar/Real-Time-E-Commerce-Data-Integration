import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('<Table Name>')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['kinesis']['data'].encode('utf-8'))
        print(f"Processing: {payload}")

        table.put_item(
            Item={
                "Item_ID": payload["Item_ID"],
                "Timestamp": payload["Timestamp"],
                "Item_Name": payload["Item_Name"],
                "Click_Counts": payload["Click_Counts"]
            }
        )

    return {"statusCode": 200, "body": "Processed clickstream batch"}
