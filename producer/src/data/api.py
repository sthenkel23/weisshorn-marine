import pandas as pd
import requests

def fetch_data_cb_api(df):
    """

    :return: _description_
    :rtype: pd.DataFrame
    """
    response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    r = response.json()["data"]
    r["timestamp"] = pd.to_datetime("today").now()
    if df.empty:
        df = pd.DataFrame([r])
        return df
    else:
        return df.append(r, ignore_index=True)
    return None
