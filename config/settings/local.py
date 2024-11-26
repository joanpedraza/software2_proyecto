from .base import *

DEBUG = True

ENVIROMENT = "local"

INSTALLED_APPS += [
    'django_browser_reload',
]

MIDDLEWARE += [
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = env("NPM_BIN_PATH", default="C:/Program Files/nodejs/npm.cmd")

API_BASE_URL = env("API_BASE_URL", default="http://localhost:8000")
