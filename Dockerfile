FROM python:3.9-slim

# RUN useradd -d /home/docker_user -m -s /bin/bash docker_user
# USER docker_user

# RUN mkdir -p /home/docker_user/workspace
# WORKDIR /home/docker_user/workspace

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY src/dist/marine-0.0.0.1-py3-none-any.whl ./marine-0.0.0.1-py3-none-any.whl
RUN pip3 install marine-0.0.0.1-py3-none-any.whl


COPY gcl.json ./gcl.json

COPY src/dashboard.py .
CMD streamlit run --server.port $PORT dashboard.py
