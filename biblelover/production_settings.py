import os
import dj_database_url
from biblelover.settings.base_setting import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = get_env_variable('SECRET_KEY')

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(
    get_env_variable('DATABASE_URL'), conn_max_age=600)


# Sending email configuration
EMAIL_HOST_USER = get_env_variable("ADMIN_EMAIL_ADDRESS")

EMAIL_HOST_PASSWORD = get_env_variable("ADMIN_EMAIL_PASSWORD")

EMAIL_PORT = get_env_variable("EMAIL_PORT")

EMAIL_HOST = get_env_variable("EMAIL_HOST")

EMAIL_USE_TLS = True

# Admin email configuration
ADMIN_EMAILS = [
    [get_env_variable("ADMIN_FULL_NAME"), get_env_variable("ADMIN_EMAIL_ADDRESS")]]

ADMINS = ADMIN_EMAILS

MANAGERS = ADMIN_EMAILS

ADMIN_URL = get_env_variable("ADMIN_URL")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'biblelover/assets'),
]
