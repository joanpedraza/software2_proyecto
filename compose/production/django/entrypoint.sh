#!/bin/sh

# Instalar dependencias de npm y construir archivos estáticos
npm install
npm install -g yarn
yarn run build

# Aplicar migraciones de la base de datos
python manage.py migrate

# Recoger archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar gunicorn con el archivo WSGI de tu proyecto
exec gunicorn --env DJANGO_SETTINGS_MODULE=config.settings config.wsgi:application --bind 0.0.0.0:8000
