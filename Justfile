set dotenv-load

clean:
    rm -rf dist

build:
    poetry build

deps:
    poetry install --no-interaction --with=dev

test:
    poetry run pytest

isort:
    poetry run isort src tests

black:
    poetry run black src tests

format: isort black

lint:
    poetry run ruff check src tests
    poetry run pyright src tests
