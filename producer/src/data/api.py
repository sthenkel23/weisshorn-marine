from datetime import datetime

import requests


def fetch_data_cb_api_continuously():
    """

    :return: _description_
    :rtype: pd.DataFrame
    """
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot", timeout=10)
    r = response.json()["data"]
    r["timestamp"] = str(datetime.utcnow())
    return response, r
