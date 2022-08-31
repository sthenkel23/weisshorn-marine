import pandas as pd
import streamlit as st
import requests

DATASET_URL = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"


@st.experimental_memo
def fetch_data() -> pd.DataFrame:
    """_summary_

    :return: _description_
    :rtype: pd.DataFrame
    """
    return pd.read_csv(DATASET_URL)


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
