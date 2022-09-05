IMAGE := marine
VERSION := latest
APP := consumer

install:
	pip install --upgrade pip && \
		pip install -r consumer/requirements.txt && \
		pip install -r producer/requirements.txt && \
		pip install -r requirements-test.txt

lint:
	pylint --disable=C,E0611,R0903,E1136 $$(git ls-files '*.py')

format:
	black $$(git ls-files '*.py')

sort:
	isort $$(git ls-files '*.py')

mypy:
	mypy $$(git ls-files '*.py')

testing:
	python -m pytest -vv --cov=${APP}/src tests/*.py

profile-test:
	python -m pytest -vv --durations=1 --durations-min=1.0 --cov=${APP}/src tests/*.py

parallel-test:
	python -m pytest -vv -n auto --dist loadgroup tests/*.py

test: install sort format lint testing


create-virtual:
	python3 -m venv ~/.env

source-virtual:
	source ~/.env/bin/activate

build-pypi:
	pip install --upgrade pip
	pip install build
	python3 -m build 

.PHONY: run-app
run-app:
	streamlit run consumer/src/dashboard.py

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
	docker build --build-arg BACKEND_NAME=${BACKEND_NAME} \
		-t $(IMAGE):$(VERSION) . \
		-f ./${APP}/Dockerfile \

.PHONY: clean_docker
clean_docker:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

.PHONY: clean_build
clean_build:
	rm -rf build/

.PHONY: clean
clean: clean_build clean_docker