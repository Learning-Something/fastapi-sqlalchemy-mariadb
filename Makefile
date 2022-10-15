tests:
	docker-compose exec todo_list tests

tests-local:
	doppler run -- pytest

up:
	docker-compose up

migrate-revision:
	export PYTHONPATH=$PWD/src
	python database/migrations/revision.py

migrate-upgrade:
	export PYTHONPATH=$PWD/src
	python database/migrations/upgrade.py

pc-config:
	pre-commit install --install-hooks

pc-after-commit:
	pre-commit run --from-ref origin/HEAD --to-ref HEAD

pc-run-all:
	pre-commit run --all-files

pc-run:
	pre-commit run

bash:
	docker-compose exec app bash

shell:
	export PYTHONPATH=$PWD/src
	doppler run -- ipython
