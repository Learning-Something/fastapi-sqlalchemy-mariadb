# Todo List with SQLAlchemy and MariaDB

This is a simple todo list application using SQLAlchemy and MariaDB.

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- [MariaDB](https://mariadb.org/) - MariaDB is an open source relational database management system (RDBMS) based on MySQL.
- [SQLAlchemy AsyncIO + asyncmy](https://github.com/long2ice/asyncmy) - SQLAlchemy dialect for MySQL/MariaDB with asyncio support.
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.
- [Docker](https://www.docker.com/) - Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.
- [New Relic](https://newrelic.com/) - New Relic is a SaaS-based application performance management (APM) software platform that provides real-time insights into application performance and user experience.
- [Pytest](https://docs.pytest.org/en/stable/) - Pytest is a testing framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
- [Pytest-asyncio](https://pypi.org/project/pytest-asyncio/) - Pytest-asyncio is a plugin for pytest that allows you to write tests using asyncio coroutines.
- [Pre-commit](https://pre-commit.com/) - Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks.
- [Python Decouple](https://pypi.org/project/python-decouple/) - Python Decouple is a straightforward solution for storing your settings in environment variables and retrieving them as Python objects.
- [Poetry](https://python-poetry.org/) - Poetry is a dependency manager for Python that allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

## Requirements

- [Python 3.10](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Poetry](https://python-poetry.org/docs/#installation)

### Local Libraries (Optional)

- [Pre-commit](https://pre-commit.com/#install) (Automatically run linters and formatters)
- [MariaDB Connector/C](https://downloads.mariadb.org/connector-c/) (MariaDB Connector/C is required for the `mysqlclient` library)
- [Pylint](https://pypi.org/project/pylint/) (Python linter)
- [Mypy](https://pypi.org/project/mypy/) (Python static type checker)
- [Alembic](https://pypi.org/project/alembic/) (Database migration tool)

## Folder Structure

```
/.ignore # Local database files (ignored by git)
/src  # Source code
    /database  # Database connection, migrations and base model
    /exceptions  # Global exceptions
    /routes  # API routes
    /utils  # Utility functions
    /packages  # Domain and business logic
        /todo_list  # Todo list domain
            /models  # Todo list models
            /repositories  # Todo list repositories
            /services  # Todo list services
            /schemas  # Todo list schemas
            /exceptions  # Todo list exceptions
            /routes  # Todo list routes
            /tests  # Todo list unit tests
    app.py  # Main application
    settings.py  # Application settings
    conftest.py  # Pytest configuration
.editorconfig  # Editor configuration
.env  # Environment variables (ignored by git)
.env-example  # Environment variables example
.flake8  # Flake8 configuration
.gitignore  # Git ignore configuration
.pre-commit-config.yaml  # Pre-commit configuration
.pylintrc  # Pylint configuration
docker-compose.yml  # Docker compose configuration
Dockerfile  # Dockerfile
logging.ini  # Logging configuration
Makefile  # Makefile with common commands
mypy.ini  # Mypy configuration
newrelic.ini  # New Relic configuration
poetry.lock  # Poetry lock file
pyproject.toml  # Poetry configuration
README.md  # This file
start.sh  # Start script
```

## Running the Application

### Docker

- Put your `DOPPLER_TOKEN` in the `.env` file
- Run `docker-compose up` or `make up` to start the application

### Local

- Put your `DOPPLER_TOKEN` in the `.env` file
- Run `poetry install` to install the dependencies
- Run `poetry run alembic upgrade head` to run the database migrations
- Run `./start.sh` to start the application

## Running the Tests

### Docker

- Run `docker-compose up` to start the application and MariaDB database
- Run `docker-compose exec todo_list tests` to run the tests

### Local

- Run `poetry install` to install the dependencies
- Run `make migrate-upgrade` to run the database migrations
- Run `doppler run -- pytest` to run the tests

## API Documentation

### Production

- [Swagger](http://todo-list.nereswe.com/docs)
- [ReDoc](http://todo-list.nereswe.com/redoc)

### Local

- [Swagger](http://localhost:5000/docs)
- [ReDoc](http://localhost:5000/redoc)

## Adding new libraries

- Run `poetry add <library>` to add a new library to production
- Run `poetry add <library> -G dev` to add a new library to development
