FROM python:3.9-slim

RUN useradd -d /home/docker_user -m -s /bin/bash docker_user
USER docker_user

RUN mkdir -p /home/docker_user/workspace
WORKDIR /home/docker_user/workspace

# WORKDIR /app
ENV PATH="${PATH}:/home/docker_user/.local/bin"
RUN python3 -m venv ./venv
RUN . ./venv/bin/activate && python3 -m pip install --upgrade pip

COPY producer/requirements.txt ./requirements.txt
RUN . ./venv/bin/activate && pip install -r requirements.txt

COPY dist/marine-0.0.0.1-py3-none-any.whl ./marine-0.0.0.1-py3-none-any.whl
RUN  . ./venv/bin/activate && pip install marine-0.0.0.1-py3-none-any.whl --upgrade

ADD ./ .
CMD  . ./venv/bin/activate && uvicorn producer.src.main:app --host 0.0.0.0 --port $PORT
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
