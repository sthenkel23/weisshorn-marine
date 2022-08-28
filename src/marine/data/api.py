import pandas as pd
DATASET_URL = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"


def fetch_data() -> pd.DataFrame:
    """_summary_

    :return: _description_
    :rtype: pd.DataFrame
    """
    return pd.read_csv(DATASET_URL)
