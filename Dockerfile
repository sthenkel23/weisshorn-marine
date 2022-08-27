FROM python:3.9-slim
# EXPOSE 8501
RUN apt update && apt install -y make
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && \
		pip install -r requirements.txt 
COPY src/marine/app.py .
CMD streamlit run --server.port $PORT app.py
