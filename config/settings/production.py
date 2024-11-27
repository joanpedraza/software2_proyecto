from .base import *

# Debug desactivado
DEBUG = False
ENVIROMENT = "production"

# Seguridad
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# X_FRAME_OPTIONS = "DENY"

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
CORS_ALLOW_ALL_ORIGINS = True

# WhiteNoise para archivos estáticos
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Hosts y CSRF
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['software2proyecto-production.up.railway.app'])
CSRF_TRUSTED_ORIGINS = [
    'https://software2proyecto-production.up.railway.app',
    'https://invencloud.up.railway.app',
]

# Cabecera para proxies como Railway
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

API_BASE_URL = env("API_BASE_URL", default="https://invencloud.up.railway.app")

WHITE_NOISE_BROTLI = True 

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='AKXXXXXXXXXOOAHL')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='qdnknt66ZsdrR')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='test-bucket')

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
