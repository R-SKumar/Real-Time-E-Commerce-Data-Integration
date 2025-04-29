import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('<Table Name>')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['kinesis']['data'].encode('utf-8'))
        print(f"Processing: {payload}")
        
        truck_id = payload["truck_id"]
        timestamp = datetime.utcnow().isoformat()

        payload["Truck_ID"] = truck_id
        payload["Timestamp"] = timestamp

        table.put_item(Item=payload)

    return {"statusCode": 200, "body": "Processed telemetry batch"}
