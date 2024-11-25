from .base import *

# Debug desactivado
DEBUG = False

# Seguridad
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = "DENY"

# Archivos estáticos y media
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Hosts y CSRF
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['software2proyecto-production.up.railway.app'])
CSRF_TRUSTED_ORIGINS = [
    'https://software2proyecto-production.up.railway.app',
    'https://invencloud.up.railway.app',
]

# Cabecera para proxies como Railway
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

API_BASE_URL = env("API_BASE_URL", default="https://invencloud.up.railway.app")
