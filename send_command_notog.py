import asyncio
import websockets

# async def send_websocket_message(state): 
def send_websocket_message(state): 

    # async with websockets.connect('ws://example.com:8080') as websocket:
    with websockets.connect('ws://192.168.0.100:1880/test') as websocket:
    
        # while True:
            # message = input("Enter a message to send (or type 'exit' to quit): ")
        message = state
        # if message.lower() == 'exit':
        #     break
        websocket.send(message)

if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(send_websocket_message())
    pass