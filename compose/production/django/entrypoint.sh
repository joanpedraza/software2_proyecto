#!/bin/sh

# Limpiar archivos estáticos antiguos (si es necesario)
echo "Aplicando migraciones de la base de datos..."
python manage.py migrate

#!/bin/sh
echo "Verificando la configuración de Nginx..."
nginx -t

echo "Verificando el contenido de los directorios..."
ls -l /app/static
ls -l /app/media


# Iniciar Supervisor
echo "Iniciando Supervisor..."
exec /usr/bin/supervisord -c /etc/supervisord.conf
