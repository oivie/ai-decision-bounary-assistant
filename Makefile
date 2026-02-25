# Makefile for AI Decision Boundary Assistant

.PHONY: help install dev-install test lint format type-check run clean build docs

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install production dependencies"
	@echo "  dev-install  - Install development dependencies"
	@echo "  test         - Run test suite"
	@echo "  lint         - Run code linting"
	@echo "  format       - Format code with black"
	@echo "  type-check   - Run type checking with mypy"
	@echo "  run          - Start the application"
	@echo "  clean        - Clean build artifacts"
	@echo "  build        - Build distribution packages"
	@echo "  docs         - Generate documentation"

# Installation
install:
	pip install -r requirements.txt

dev-install: install
	pip install -e .[dev]

# Testing
test:
	PYTHONPATH=src python3 -m pytest tests/ -v

test-cov:
	PYTHONPATH=src python3 -m pytest tests/ --cov=ai_decision_assistant --cov-report=html

# Code quality
lint:
	flake8 src/ tests/ examples/

format:
	black src/ tests/ examples/

format-check:
	black --check src/ tests/ examples/

type-check:
	mypy src/

# Application
run:
	PYTHONPATH=src python3 run_app.py

demo:
	PYTHONPATH=src python3 -m streamlit run src/ai_decision_assistant/ui/app.py --server.port=8501

example:
	PYTHONPATH=src python3 examples/basic_usage.py

cli-demo:
	PYTHONPATH=src python3 cli.py --text "I think we should launch the crypto feature next week. Mike can you handle compliance?"

# Maintenance
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .coverage htmlcov/ .pytest_cache/ .mypy_cache/

# Building
build: clean
	python setup.py sdist bdist_wheel

# Development workflow
dev-setup: dev-install
	@echo "Setting up pre-commit hooks..."
	@if command -v pre-commit >/dev/null 2>&1; then \
		pre-commit install; \
	else \
		echo "pre-commit not found. Install with: pip install pre-commit"; \
	fi

# Quality checks (run before committing)
check: format-check lint type-check test
	@echo "All quality checks passed!"

# Quick development cycle
dev: format lint test
	@echo "Development cycle complete!"
