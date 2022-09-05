import asyncio
from random import choice, randint
import json
from data.api import fetch_data_cb_api_continuously
from data.data_model import Item
from data.items import items
from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.get("/")
def index():
    return {
        "message": "This is the home page of this API. Go to /apiv1/ or /apiv2/?name="
    }


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


@app.get("/apiv1/{name}")
def api1(name: str):
    return {"message": f"Hello! @{name}"}


@app.get("/apiv2/")
def api2(name: str):
    return {"message": f"Hello! @{name} with"}


CHANNELS = ["A", "B", "C"]


@app.websocket("/sample")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        _, r = fetch_data_cb_api_continuously()
        # if res:
        r.update({"channel": choice(CHANNELS), "data": randint(1, 10)})
        # else:
        #     r = {"channel": choice(CHANNELS), "data": randint(1, 10)}
        # print(res.text, r)
        # r = {"channel": choice(CHANNELS), "data": randint(1, 10)}
        await websocket.send_json(json.dumps(r))
        await asyncio.sleep(0.5)


# if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=4000, debug=True)
