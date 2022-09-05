import requests
import pandas as pd


def fetch_data_cb_api_continuously():
    """

    :return: _description_
    :rtype: pd.DataFrame
    """
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    r = response.json()["data"]
    r["timestamp"] = pd.to_datetime("today").now()
    return pd.DataFrame([r])