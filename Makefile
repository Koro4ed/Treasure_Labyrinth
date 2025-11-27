.PHONY: install project lint build

install:
	poetry install

project: install
	@echo "Project setup complete"

lint:
	poetry run ruff check .

build:
	poetry build
