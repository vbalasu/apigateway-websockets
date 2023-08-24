import json

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']
    print(connection_id)
    import boto3
    dynamodb = boto3.client('dynamodb')
    dynamodb.delete_item(TableName="connections",Key={
                "connection_id": {
                    "S": connection_id
                }
            }
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Connected')
    }
