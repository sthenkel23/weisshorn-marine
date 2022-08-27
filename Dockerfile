FROM python:3.9-slim
# EXPOSE 8501
ARG var
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip && \
		pip install -r requirements.txt 
COPY src/$(var)/app.py .
CMD streamlit run --server.port $PORT app.py
