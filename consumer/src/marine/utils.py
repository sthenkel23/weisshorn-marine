from collections import defaultdict, deque
from functools import partial
from os import getenv

import aiohttp

HEROKU_BACKEND_NAME = "weisshorn-backend"

if getenv("IS_DOCKERIZED"):
    WS_CONN = f"ws://{HEROKU_BACKEND_NAME}.herokuapp.com/sample"
else:
    WS_CONN = "ws://127.0.0.1:8000/sample"


async def consumer(graphs, window_size, status):
    windows = defaultdict(partial(deque, [0] * window_size, maxlen=window_size))

    async with aiohttp.ClientSession(trust_env=True) as session:
        status.subheader(f"Connecting to {WS_CONN}")
        async with session.ws_connect(WS_CONN) as websocket:
            status.subheader(f"Connected to: {WS_CONN}")
            async for message in websocket:
                data = message.json()

                windows[data["channel"]].append(data["data"])

                for channel, graph in graphs.items():
                    channel_data = {channel: windows[channel]}
                    if channel == "A":
                        graph.line_chart(channel_data)
                    elif channel == "B":
                        graph.area_chart(channel_data)
                    elif channel == "C":
                        graph.bar_chart(channel_data)
