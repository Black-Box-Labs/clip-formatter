project = formatter

install-dev:
	poetry lock --no-update
	poetry install --with dev

format:
	poetry run ruff check ${project} tests

tests:
	poetry run pytest -v tests

coverage:
	poetry run pytest --cov ${project} --cov-report term-missing tests --disable-warnings --cov-fail-under=60

run-ci: format coverage