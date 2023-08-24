import json

def lambda_handler(event, context):
    print('event', event)
    print('context', context)
    endpoint_url = 'https://' + event['requestContext']['domainName'] + '/' + event['requestContext']['stage']
    body = json.loads(event['body'])
    if 'to' in body:
        connection_id = body['to']
    else:
        connection_id = event['requestContext']['connectionId']
    print('connection_id', connection_id)
    print('endpoint_url', endpoint_url)
    print('body', event['body'])

    if event['requestContext']['routeKey'] == 'message':
        push(connection_id, endpoint_url, event['body'])
    elif event['requestContext']['routeKey'] == 'broadcast':
        for connection in get_connections():
            push(connection, endpoint_url, event['body'])
    elif event['requestContext']['routeKey'] == 'whoami':
        push(connection_id, endpoint_url, json.dumps({'connectionId': connection_id}))
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def push(connection_id, endpoint_url, data):
    import boto3
    apig = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint_url)
    apig.post_to_connection(Data=data, ConnectionId=connection_id)
    
def get_connections():
    import boto3
    dynamodb = boto3.client('dynamodb')
    items = dynamodb.scan(TableName='connections')['Items']
    return [i['connection_id']['S'] for i in items]