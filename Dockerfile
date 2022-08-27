FROM python:3.9-slim
# EXPOSE 8501
RUN adduser myuser
USER myuser

WORKDIR /app
RUN pip install --upgrade pip
ARG lib=marine

COPY --chown=myuser:myuser requirements.txt ./requirements.txt
RUN pip install --user -r requirements.txt 
ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser src/${lib}/app.py .
CMD streamlit run --server.port $PORT app.py
