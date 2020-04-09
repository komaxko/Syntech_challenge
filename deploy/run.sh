#!/bin/sh

python ./manage.py migrate --configuration Dev && \
  ./manage.py collectstatic --noinput && \
  ./manage.py create_templates --configuration Dev && \
  ./manage.py runserver 0.0.0.0:8000 --configuration Dev
