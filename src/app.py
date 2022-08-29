#!/usr/bin/env python

from summa import summarizer
import streamlit as st

import time

from db.firestore import doc
from marine.data.api import fetch_data


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


# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())


# creating a single-element container.
placeholder = st.empty()

with placeholder.container():
    st.markdown("### Detailed Data View")
    df = fetch_data()
    st.dataframe(df)
    time.sleep(1)
