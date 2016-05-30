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

DEBUG = False
ALLOWED_HOSTS = ['*']

DB_USER = get_env_variable('DB_USER')
DB_PASS = get_env_variable('DB_PASS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'filmy',
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': 'whateez-142.postgres.pythonanywhere-services.com',
        'PORT': '10142',
    }
}
