.PHONY: lint test check

lint:
	flake8

test:
	pytest --cov=app

check: lint test
