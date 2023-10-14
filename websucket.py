import websocket

def send_websock(message):
    # Define the WebSocket server URL
    websocket_url = 'ws://192.168.0.100:1880/test'

    # Create a WebSocket connection
    ws = websocket.WebSocket()

    # Connect to the WebSocket server
    ws.connect(websocket_url)

    ws.send(message)

    # ws.close()

