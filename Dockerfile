FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/code/src
ENV NEW_RELIC_CONFIG_FILE=/code/newrelic.ini

RUN apt update -y && apt install -y curl gcc gnupg2 make

RUN curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | apt-key add - \
  && echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list
RUN apt update -y && apt install -y doppler

RUN apt install --no-install-recommends -y ca-certificates locales locales-all \
  && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
  && update-ca-certificates \
  && echo 'America/Sao_Paulo' > /etc/timezone \
  && rm -rf /var/lib/apt/lists/*

RUN locale-gen pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt_br
ENV LC_ALL pt_BR.UTF-8

RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
RUN curl -L https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash

RUN apt-get update
RUN apt-get install libmariadb3 libmariadb-dev -yy

RUN mkdir /code
WORKDIR /code

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install --no-cache -U poetry && poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi -vvv

COPY . .

ENTRYPOINT ["doppler", "run", "--"]

CMD ["./start.sh"]
