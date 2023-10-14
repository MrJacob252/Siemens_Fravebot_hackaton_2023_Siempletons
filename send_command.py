import asyncio
import websockets

async def send_websocket_message():
    async with websockets.connect('ws://example.com:8080') as websocket:
        while True:
            message = input("Enter a message to send (or type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            await websocket.send(message)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(send_websocket_message())