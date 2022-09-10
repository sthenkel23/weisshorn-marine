#!/usr/bin/env python
import asyncio
import streamlit as st
from db.firestore import collection, doc
from marine.utils import consumer_alerts_handling


st.set_page_config(page_title="marine-alerts", layout="wide")

status = st.empty()

asyncio.run(
    consumer_alerts_handling(
        status,
    )
)


st.title("Past alerts")
st.subheader("Meta information breakdown:")
st.text("Alert: ...")
d = {}
for doc in collection.stream():
    post = doc.to_dict()
    # ids = post["id"]
    amount = post["amount"]
    timestamp = post["timestamp"]

    st.subheader(f"Alert: {doc.id}")
    st.write(f"Alert Amount: {amount}")
    st.write(f"Timestamp: {timestamp}")
    # st.write(f"ID: {ids}")
    d[doc.id] = doc.to_dict()
