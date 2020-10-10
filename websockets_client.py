#! /usr/bin/env python
# WS server example

import asyncio
import websockets

async def hello():
    uri = 'WS://localhost:8765'
    async with websockets.connect(uri) as websocket:
        #name = await websocket.recv()
        name = "clientx"
        print(f" < {name} ")

        greeting = f"Hello {name}"

        await websocket.send(name)
        print(f"> {name}")
        greeting = await websocket.recv()
        print(f"< {greeting}")

#start_server = websockets.serve(hello, "localhost", 8769)

#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()

asyncio.get_event_loop().run_until_complete(hello())

