DATA="hello from server"
CONNECTION_ID=JbeM9fUeoAMCLeg=
ENDPOINT_URL=https://bonxj0rcm9.execute-api.us-east-1.amazonaws.com/production

aws apigatewaymanagementapi post-to-connection --data "$DATA" --connection-id $CONNECTION_ID --endpoint-url $ENDPOINT_URL --profile websockets-role
