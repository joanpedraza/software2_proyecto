#!/bin/bash

set -o errexit  # Salir si un comando falla
set -o pipefail # Hacer que un pipe falle si un comando en el pipe falla
set -o nounset  # Salir si se intenta usar una variable no definida

# Limpiar archivos estáticos antiguos (opcional)
# echo "Limpiando archivos estáticos antiguos..."
# rm -rf staticfiles/*
# rm -rf app/static/bundles/*

# Preparar la base de datos y archivos estáticos
echo "Aplicando migraciones de la base de datos..."
python manage.py makemigrations
python manage.py migrate

# Recopilar archivos estáticos
echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# Ejecutar Gunicorn
PORT=${PORT:-8080}  # Cambiado a 8080 por defecto
echo "Iniciando Gunicorn en el puerto $PORT..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 60