#!/bin/sh

# Limpiar archivos estáticos antiguos (si es necesario)
echo "Aplicando migraciones de la base de datos..."
python manage.py migrate

# Iniciar Supervisor
echo "Iniciando Supervisor..."
exec /usr/bin/supervisord -c /etc/supervisord.conf
