# apigateway-websockets

This repository contains code for an API Gateway named `websocket-publisher` with the following routes:

1. connect - [websocket-publisher-connect](websocket-publisher-connect/lambda_function.py)
2. disconnect - [websocket-publisher-disconnect](websocket-publisher-disconnect/lambda_function.py)
3. broadcast, message, whoami - [websocket-publisher](websocket-publisher/lambda_function.py)

Multiple clients can connect to the [websocket endpoint](wss://bonxj0rcm9.execute-api.us-east-1.amazonaws.com/production) and pass messages to each other. 