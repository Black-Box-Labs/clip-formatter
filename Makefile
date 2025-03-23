project = formatter

install-dev:
	poetry lock --no-update
	poetry install --with dev

check:
	poetry run ruff format ${project} --check
	poetry run ruff check ${project}

format:
	poetry run ruff format ${project}

tests:
	poetry run pytest -v tests

coverage:
	poetry run pytest --cov ${project} --cov-report term-missing tests --disable-warnings --cov-fail-under=60

run-ci: check coverage