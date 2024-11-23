#!/bin/sh

npm install
npm install -g yarn
yarn run build

python manage.py migrate
python manage.py collectstatic --noinput

# Discomment to a lot funtions debugger but not working socket channels
# to do: Whats happend in sockket?
# exec python manage.py runserver_plus 0.0.0.0:8000

exec python manage.py runserver 0.0.0.0:8000

#echo 'Running server...'
#gunicorn --env DJANGO_SETTINGS_MODULE=config.settings config.wsgi:application --bind 0.0.0.0:$PORT
