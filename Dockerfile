FROM python:3.9-slim
# EXPOSE 8501
RUN apt update && apt install -y make

ARG var
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY Makefile ./Makefile
CMD make install
COPY src/$var/app.py .
CMD streamlit run --server.port $PORT app.py
