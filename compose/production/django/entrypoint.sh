#!/bin/sh

# Aplicar migraciones de la base de datos
python manage.py migrate

# Instalar Gunicorn si no está instalado
if ! pip show gunicorn > /dev/null 2>&1; then
    echo "Instalando Gunicorn..."
    pip install gunicorn
fi

PORT=${PORT:-8000} 

# Ejecutar Gunicorn con el archivo WSGI de tu proyecto
exec gunicorn config.wsgi:application --workers 3 --timeout 60 --bind 0.0.0.0:$PORT
