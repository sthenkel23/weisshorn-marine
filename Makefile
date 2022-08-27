LIB_NAME=${{ secrets.LIB_NAME }}


install:
	pip install --upgrade pip && \
		pip install -r requirements.txt && \
		pip install -r requirements-test.txt
lint:
	pylint --disable=C $$(git ls-files '*.py')

format:
	black $$(git ls-files '*.py')

testing:
	python -m pytest -vv --cov=src/$(LIB_NAME) tests/*.py

profile-test:
	python -m pytest -vv --durations=1 --durations-min=1.0 --cov=src/mylib tests/*.py

parallel-test:
	python -m pytest -vv -n auto --dist loadgroup tests/*.py

test: install format lint testing


create-virtual:
	python3 -m venv ~/.env

source-virtual:
	source ~/.env/bin/activate

run-app:
	streamlit run src/marine/app.py
