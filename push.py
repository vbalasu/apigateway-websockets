data = "hello from python"
connection_id = 'JZgfFeBjIAMCJuQ='
endpoint_url = 'https://bonxj0rcm9.execute-api.us-east-1.amazonaws.com/production'

import boto3
apig = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint_url)
apig.post_to_connection(Data=data, ConnectionId=connection_id)
