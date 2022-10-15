#!/bin/bash
echo alias shell="'doppler run -- ipython'" >> ~/.bashrc
echo alias tests="'doppler run -- pytest --cov'" >> ~/.bashrc

echo "Rodando o servidor"
if test $ENVIRONMENT = 'development' ; then
  python -m debugpy --listen 0.0.0.0:5678 -m \
    uvicorn app:create_app --factory \
    --host 0.0.0.0 --port 5000 \
    --log-level debug --log-config logging.ini \
    --reload --reload-dir $PWD/src --reload-include '*.py'
else
  newrelic-admin run-program \
    uvicorn app:create_app --factory \
    --host 0.0.0.0 --port 5000 \
    --log-level info --log-config logging.ini \
    --workers 1
fi
