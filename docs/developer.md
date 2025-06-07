# Developer Guide

## Local Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Quality Checks

Run flake8 and the test suite with coverage using the Makefile:

```bash
make check
```

This will execute:

```bash
flake8
pytest --cov=app
```
