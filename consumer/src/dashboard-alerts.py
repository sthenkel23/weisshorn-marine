#!/usr/bin/env python
import asyncio

import streamlit as st
from marine.utils import consumer_alerts_handling

st.set_page_config(page_title="marine-alerts", layout="wide")

status = st.empty()

asyncio.run(
    consumer_alerts_handling(
        status,
    )
)
