# Base de Python para la aplicación
FROM python:3.11-slim AS python-base

# Establecer directorio de trabajo
WORKDIR /app

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    BUILD_ENV=production

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Actualizar pip
RUN pip install --upgrade pip

# Copiar dependencias de Python
COPY ./requirements.txt ./production.txt /app/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r production.txt

# ---- Etapa para Tailwind y Node.js ---- #
FROM node:20.18.1-slim AS node-build

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios para Tailwind
COPY ./theme/static_src/package.json ./theme/static_src/
COPY ./theme/static_src/postcss.config.js ./theme/static_src/
COPY ./theme/static_src/tailwind.config.js ./theme/static_src/
COPY ./theme/static_src/src/styles.css ./theme/static_src/src/

# Copiar el directorio frontend
COPY ./frontend ./frontend/

# Instalar dependencias de Node.js
WORKDIR /app/theme/static_src
RUN yarn install --frozen-lockfile

# Ejecutar la construcción de Tailwind
RUN yarn run build

# Cambiar de nuevo al directorio de trabajo principal
WORKDIR /app/frontend

# Copiar el package.json y yarn.lock del frontend
COPY ./package.json ./yarn.lock ./

# Instalar dependencias de Node.js para SCSS
RUN yarn install --frozen-lockfile

# Ejecutar la construcción de SCSS
RUN yarn run build

WORKDIR /app


# Copiar los archivos de salida de la compilación (si es necesario)
COPY ./static ./static

# ---- Finalizar imagen ---- #
FROM python-base

# Copiar archivos compilados de Node.js (Tailwind y SCSS)
COPY --from=node-build /app/theme/static /app/theme/static
COPY --from=node-build /app/static /app/static

# Copiar el resto del proyecto
COPY . /app/

# Todo: Instalar Node.js y npm globalmente
ARG NODE_MAJOR=18

RUN mkdir -p /etc/apt/keyrings && \
  curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
  echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_${NODE_MAJOR}.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list && \
  apt-get update && apt-get install -y nodejs && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Verificar la instalación de npm y node
RUN npm --version
RUN node --version
RUN which npm
RUN which node


# Instalar dependencias de Node.js usando npm
WORKDIR /app/theme/static_src
RUN npm install --frozen-lockfile

# Ejecutar la construcción de Tailwind usando npm
RUN npm run build


# Asegurar que Django detecte npm
ENV PATH="/usr/bin:$PATH"
ENV NPM_BIN_PATH="/usr/bin/npm"
#ENV NPM_BIN_PATH="/usr/local/bin/yarn"

# Ejecutar la construcción de Tailwind
RUN python manage.py tailwind build

# Recoger archivos estáticos
RUN python manage.py collectstatic --noinput

# Copiar el entrypoint.sh
COPY ./compose/production/django/entrypoint.sh /compose/production/django/entrypoint.sh

# Configuración del puerto
EXPOSE 8000

# Comando de inicio
CMD ["sh", "/compose/production/django/entrypoint.sh"]
