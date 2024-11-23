FROM python:3.11.10-alpine3.20

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ARG APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Actualizar paquetes del sistema e instalar dependencias necesarias
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev \
    curl \
    nodejs \
    npm \
    git \
    g++ \
    make && \
    pip install --upgrade pip

# Instalar dependencias de Python desde requirements.txt
COPY ./production.txt ./
RUN pip install -r production.txt && pip install gunicorn

RUN npm install -g yarn

# Copiar el código de la aplicación al contenedor
COPY ./ ./

# Configurar el comando predeterminado
CMD ["sh", "entrypoint.sh"]

# Descomenta para ejecutar directamente Django
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]