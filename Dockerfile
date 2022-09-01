FROM python:3.9-slim

RUN useradd -d /home/docker_user -m -s /bin/bash docker_user
USER docker_user

RUN mkdir -p /home/docker_user/workspace
WORKDIR /home/docker_user/workspace

# WORKDIR /app
ENV PATH="${PATH}:/home/docker_user/.local/bin"
RUN python3 -m venv /opt/venv
RUN  /opt/venv/bin/activate && python3 -m pip3 install --upgrade pip

COPY requirements.txt ./requirements.txt
RUN  /opt/venv/bin/activate && pip3 install -r requirements.txt

COPY src/dist/marine-0.0.0.1-py3-none-any.whl ./marine-0.0.0.1-py3-none-any.whl
RUN  /opt/venv/bin/activate && pip3 install marine-0.0.0.1-py3-none-any.whl


COPY gcl.json ./gcl.json

COPY src/dashboard.py .
CMD  /opt/venv/bin/activate && streamlit run --server.port $PORT dashboard.py
