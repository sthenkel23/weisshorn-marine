FROM python:3.9-slim
# EXPOSE 8501
RUN apt update && apt install -y make
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
RUN make install
COPY src/marine/app.py .
CMD streamlit run --server.port $PORT app.py
