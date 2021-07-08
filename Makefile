install:
	poetry install

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

build:
	rm ./dist/*.whl
	rm ./dist/*.gz
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

