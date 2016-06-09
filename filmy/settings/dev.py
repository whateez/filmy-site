from .base import *
import os
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = []

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SITE_ID = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'filmy',
        'USER': 'tibu',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

INSTALLED_APPS += ('sslserver',)
