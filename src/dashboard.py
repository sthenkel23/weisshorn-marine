#!/usr/bin/env python

from summa import summarizer
import streamlit as st

import pandas as pd
import numpy as np
import time
from datetime import datetime

from db.firestore import doc, doc_ref, collection
from marine.data.api import fetch_data, fetch_data_cb_api


# Add title to the page.
st.title("Text summarization")

# Ask user for input text.
input_sent = st.text_area("Input Text", "", height=400)

# User input on what fraction of the original text to return.
ratio = st.slider(
    "Summarization fraction", min_value=0.0, max_value=1.0, value=0.2, step=0.01
)

# Summarize the original text.
summarized_text = summarizer.summarize(
    input_sent, ratio=ratio, language="english", split=True, scores=True
)

# Print out the results.
for sentence, score in summarized_text:
    st.write(sentence)


st.title("Feed firebase")
# Streamlit widgets to let a user create a new post
alert = st.text_input("Post Alert Type")
ids = st.text_input("Post ID")
description = st.text_input("Post Alert Description")
submit = st.button("Submit new alert")

if alert and description and ids and submit:
    doc_ref = collection.document(alert)
    doc_ref.set(
        {"description": description, "id": ids, "timestamp": datetime.now(tz=None)}
    )

st.title("Import firebase data by documents in collection")
d = {}
for doc in collection.stream():
    post = doc.to_dict()
    ids = post["id"]
    description = post["description"]
    timestamp = post["timestamp"]

    st.subheader(f"Alert: {doc.id}")
    st.write(f"Alert Description: {description}")
    st.write(f"Timestamp: {timestamp}")
    st.write(f"ID: {ids}")
    d[doc.id] = doc.to_dict()

st.markdown("### Detailed Data View (firebase to pandas)")
st.dataframe(pd.DataFrame(d))


st.title("Consume from continueously updating file")

placeholder = st.empty()
df = pd.DataFrame({})
val = 0.
while True:
    with placeholder.container():
        st.markdown("### Detailed Data View")
        df, val = fetch_data_cb_api(df, val)
        avg_price = np.mean(pd.to_numeric(df["amount"]))
        min_ts = np.min(df["timestamp"].astype(str))
        max_ts = np.max(df["timestamp"].astype(str))
        # Add metric elements
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(
            label="Mean Price",
            value=round(avg_price, 2),
            delta=round(avg_price) - 10,
        )
        kpi2.metric(
            label="Min timestamp",
            value=min_ts,
        )
        kpi3.metric(
            label="Max timestamp",
            value=max_ts,
        )
        st.dataframe(df)
        time.sleep(1)


st.title("Consume from static file")

# creating a single-element container.
placeholder = st.empty()

with placeholder.container():
    st.markdown("### Detailed Data View")
    df = fetch_data()
    count_married = int(
        df[(df["marital"] == "married")]["marital"].count()
        + np.random.choice(range(1, 30))
    )
    df["age_new"] = df["age"] * np.random.choice(range(1, 5))
    avg_age = np.mean(df["age_new"])

    kpi1, kpi2 = st.columns(2)
    kpi1.metric(
        label="Age ⏳",
        value=round(avg_age),
        delta=round(avg_age) - 10,
    )
    kpi2.metric(
        label="Married Count 💍",
        value=int(count_married),
        delta=-10 + count_married,
    )

    st.dataframe(df)
    time.sleep(1)
