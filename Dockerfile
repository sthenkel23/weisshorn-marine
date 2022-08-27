FROM python:3.9-slim
# EXPOSE 8501

WORKDIR /app
RUN pip install --upgrade pip
ARG lib=marine

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt 

COPY src/${lib}/app.py .
CMD streamlit run --server.port $PORT app.py
