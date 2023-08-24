# coding: utf-8
#!pip install websocket-client
import websocket
ws = websocket.WebSocket()
ws.connect('wss://bonxj0rcm9.execute-api.us-east-1.amazonaws.com/production')
def uppercase(input_string):
    return input_string.upper()
    
import json
while True:
    incoming = json.loads(ws.recv())
    if 'function' in incoming and incoming['function'] == 'uppercase':
        output = uppercase(incoming['message'])
        outgoing = {'action': 'broadcast', 'output': output}
        print(json.dumps(outgoing))
        ws.send(json.dumps(outgoing))

