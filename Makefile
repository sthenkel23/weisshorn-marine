install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

create-virtual:
	python3 -m venv ~/.env

source-virtual:
	source ~/.env/bin/activate

run-app:
	streamlit run src/marine/app.py

all: install create-virtual source-virtual run-app
