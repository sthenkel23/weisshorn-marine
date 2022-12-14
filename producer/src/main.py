import asyncio
from random import choice, randint

from data.api import fetch_data_cb_api_continuously
from data.db import collection
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


@app.post("/items/")
async def create_item(item: Item):
    """_summary_

    :param item: _description_
    :type item: Item
    :return: _description_
    :rtype: _type_
    """
    post = item.dict()
    print(f'Create a document \n {post["name"]}')
    doc_ref = collection.document(post["name"])
    print(f'Posted: \n \n {post}')
    doc_ref.set(post)
    print('Stored in db')
    return item


@app.get("/apiv1/{name}")
def api1(name: str):
    return {"message": f"Hello! @{name}"}


@app.get("/apiv2/")
def api2(name: str):
    return {"message": f"Hello! @{name} with"}


CHANNELS = ["A", "B", "C", "D"]


@app.websocket("/sample")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    event_cond = 0.0
    while True:
        res, r = fetch_data_cb_api_continuously()
        if r["amount"] != event_cond:
            if not res:
                r = {"channel": choice(CHANNELS), "data": randint(1, 10)}
            r.update({"channel": "D"})
            await websocket.send_json(r)
            await asyncio.sleep(5.0)
            event_cond = r["amount"]
        else:
            await asyncio.sleep(0.5)


# if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=4000, debug=True)
