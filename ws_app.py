import json
import asyncio
import websockets
from nsetools import Nse



async def stock_price(websocket, path):
    while True:
        stock_symbol = await websocket.recv()
        print(f"Received message: {stock_symbol}")
        nse = Nse()
        stock = nse.get_quote(stock_symbol)
        if stock is None:
            await websocket.send(json.dumps({"Error": "Invalid quote provided"}))
        else:
            price = stock["lastPrice"]
            await websocket.send(json.dumps({"price": price}))



start_server = websockets.serve(stock_price, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
