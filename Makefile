help:
	@echo make install
	@echo make format
	@echo make lint
	@echo make refactor
	@echo make test
	@echo ""
	@echo make run
	@echo ""
	@echo make container-lint
	@echo make deploy

install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

run:
	python3 main.py

test:
	# python -m pytest -vv --cov=main --cov=mylib ./tests/test_*.py
	python -m pytest -vv ./tests/test_*.py

format:	
	black main.py shapes/*.py tests/test_*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py --extension-pkg-whitelist='pydantic' main.py shapes/*.py tests/test_*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	@echo Add deploy later

	#aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	#docker build -t hello-codespace-minikube .
	#docker tag hello-codespace-minikube:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/hello-codespace-minikube:latest
	#docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/hello-codespace-minikube:latest

all: install lint test format deploy
