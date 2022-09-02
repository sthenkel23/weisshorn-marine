import pandas as pd
from fastapi import FastAPI

# import uvicorn
from data.api import fetch_data_cb_api

app = FastAPI()


@app.get("/")
def index():

    return {
        "message": "This is the home page of this API. Go to /apiv1/ or /apiv2/?name="
    }


@app.get("/apiv1/{name}")
def api1(name: str):

    return {"message": f"Hello! @{name}"}


@app.get("/apiv2/")
def api2(name: str):
    df = pd.DataFrame({})
    while True:
        df = fetch_data_cb_api(df)
        amount = df["amount"].iloc[-1]
        l = len(df)
        return {
            "message": f"Hello! @{name} with {amount} in df of size {l} see \n {df}"
        }


# if __name__ == "__main__":

#     uvicorn.run(app, host="127.0.0.1", port=4000, debug=True)
