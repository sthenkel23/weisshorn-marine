FROM python:3.9-slim
# EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && \
		pip install --user -r requirements.txt 
COPY src/marine/app.py .
CMD streamlit run --server.port $PORT app.py
