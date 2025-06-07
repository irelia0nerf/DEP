#!/bin/bash
set -e
flake8
pytest --cov=app
