FROM python:3.9-slim
# EXPOSE 8501
RUN adduser myuser
USER myuser

ARG var
WORKDIR /app
COPY --chown=myuser:myuser requirements.txt ./requirements.txt
RUN pip install --upgrade pip && \
		pip install --user -r requirements.txt 
ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser src/$var/app.py .
CMD streamlit run --server.port $PORT app.py
