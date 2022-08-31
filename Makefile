IMAGE := marine
VERSION := latest


install:
	pip install --upgrade pip && \
		pip install -r requirements.txt && \
		pip install -r requirements-test.txt

lint:
	pylint --disable=C $$(git ls-files '*.py')

format:
	black $$(git ls-files '*.py')

testing:
	python -m pytest -vv --cov=src/$(IMAGE) tests/*.py

profile-test:
	python -m pytest -vv --durations=1 --durations-min=1.0 --cov=src/mylib tests/*.py

parallel-test:
	python -m pytest -vv -n auto --dist loadgroup tests/*.py

test: install format lint testing


create-virtual:
	python3 -m venv ~/.env

source-virtual:
	source ~/.env/bin/activate

build-pypi:
	pip install --upgrade pip
	pip install build
	python3 -m build src

.PHONY: run-app
run-app:
	streamlit run src/dashboard.py

# Poetry
.PHONY: download-poetry
download-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python

.PHONY: install-poetry
install-poetry:
	poetry env use python3.7
	poetry lock -n
	poetry install -n
ifneq ($(NO_PRE_COMMIT), 1)
	poetry run pre-commit install -t pre-commit -t pre-push
endif

# Docker
.PHONY: docker
docker:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./Dockerfile

.PHONY: clean_docker
clean_docker:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

.PHONY: clean_build
clean_build:
	rm -rf build/

.PHONY: clean
clean: clean_build clean_docker