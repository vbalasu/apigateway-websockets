import json

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']
    print(connection_id)
    import boto3
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName="connections",Item={
            "connection_id": {
                "S": connection_id
            },
            "event": {
                "S": json.dumps(event)
            }
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'ConnectionId': connection_id})
    }