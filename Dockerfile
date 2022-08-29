FROM python:3.9-slim
# EXPOSE 8501
ARG KEY
WORKDIR /app
RUN pip install --upgrade pip

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY src/dist/marine-0.0.0.1-py3-none-any.whl ./marine-0.0.0.1-py3-none-any.whl
RUN pip3 install marine-0.0.0.1-py3-none-any.whl

RUN echo $KEY > g-cl.json
COPY g-cl.json ./g-cl.json

COPY src/app.py .
CMD streamlit run --server.port $PORT app.py
