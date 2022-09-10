from collections import defaultdict, deque
from functools import partial
from os import getenv

import aiohttp
from db.firestore import collection

HEROKU_BACKEND_NAME = getenv("HEROKU_BACKEND_NAME")

if getenv("IS_DOCKERIZED"):
    WS_CONN = f"ws://{HEROKU_BACKEND_NAME}.herokuapp.com/sample"
    # WS_CONN = "ws://weisshorn-backend.herokuapp.com/sample"
else:
    WS_CONN = "ws://127.0.0.1:8000/sample"


async def consumer(graphs, window_size, status):
    windows = defaultdict(partial(deque, [0] * window_size, maxlen=window_size))
    # twindows = defaultdict(partial(deque, [0] * window_size, maxlen=window_size))

    async with aiohttp.ClientSession(trust_env=True) as session:
        status.subheader(f"Connecting to {WS_CONN}")
        async with session.ws_connect(WS_CONN) as websocket:
            status.subheader(f"Connected to: {WS_CONN}")
            async for message in websocket:
                data = message.json()
                collection.document(f"alert_{data['timestamp']}").set(data)

                windows[data["channel"]].append(data["amount"])
                # twindows[data["channel"]].append(data["amount"])

                for channel, graph in graphs.items():
                    channel_data = {channel: windows[channel]}
                    if channel == "A":
                        graph.line_chart(channel_data)
                    elif channel == "B":
                        graph.area_chart(channel_data)
                    elif channel == "C":
                        graph.bar_chart(channel_data)
                    elif channel == "D":
                        graph.line_chart(channel_data)


async def consumer_alerts_handling(status):
    async with aiohttp.ClientSession(trust_env=True) as session:
        status.subheader(f"Connecting to {WS_CONN}")
        async with session.ws_connect(WS_CONN) as websocket:
            status.subheader(f"Connected to: {WS_CONN}")
            async for message in websocket:
                data = message.json()
                status.caption(f"Event Occurrence.. Stored at {data['timestamp']}")
                collection.document(f"alert_{data['timestamp']}").set(data)

                status.title("Past alerts")
                status.subheader("Meta information breakdown:")
                status.text("Alert: ...")
                d = {}
                for doc in collection.stream():
                    post = doc.to_dict()
                    # ids = post["id"]
                    amount = post["amount"]
                    timestamp = post["timestamp"]

                    status.subheader(f"Alert: {doc.id}")
                    status.write(f"Alert Amount: {amount}")
                    status.write(f"Timestamp: {timestamp}")
                    # st.write(f"ID: {ids}")
                    d[doc.id] = doc.to_dict()
