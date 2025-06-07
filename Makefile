.PHONY: lint test coverage check

lint:
	flake8 tests/test_kyc.py tests/test_engine.py tests/test_end_to_end.py --max-line-length=88 --ignore=E402

test:
	pytest tests/test_kyc.py tests/test_engine.py tests/test_end_to_end.py -q

coverage:
	coverage run -m pytest tests/test_kyc.py tests/test_engine.py tests/test_end_to_end.py -q
	coverage report

check: lint test coverage
