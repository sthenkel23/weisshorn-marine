from fastapi import FastAPI
from data.data_model import Item
from data import items

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
    return {
        "message": f"Hello! @{name} with"
    }


# if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=4000, debug=True)
