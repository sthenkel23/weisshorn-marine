import pandas as pd
import requests
import streamlit as st

DATASET_URL = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"


@st.experimental_memo
def fetch_data() -> pd.DataFrame:
    """_summary_

    :return: _description_
    :rtype: pd.DataFrame
    """
    return pd.read_csv(DATASET_URL)


def fetch_data_cb_api_continuously():
    """

    :return: _description_
    :rtype: pd.DataFrame
    """
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    r = response.json()["data"]
    r["timestamp"] = pd.to_datetime("today").now()
    return response, r


def fetch_data_cb_api(df, prev_val):
    """

    :return: _description_
    :rtype: pd.DataFrame
    """
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    r = response.json()["data"]
    r["timestamp"] = pd.to_datetime("today").now()
    if df.empty and prev_val == 0.0:
        df = pd.DataFrame([r])
        return df, r["amount"]

    if r["amount"] != df["amount"].iloc[-1]:
        return df.append(r, ignore_index=True), r["amount"]
    if r["amount"] == df["amount"].iloc[-1]:
        return df, r["amount"]
    return None


def fetch_data_backend_api(item: str):
    """

    :return: _description_
    :rtype: pd.DataFrame
    """
    response = requests.get(f"http://weisshorn-backend.herokuapp.com/items/{item}")
    r = response.json()

    return (
        pd.DataFrame([r])
        if response.status_code == 200
        else pd.DataFrame({"response": response.status_code}, index=[0])
    )
