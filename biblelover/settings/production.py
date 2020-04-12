import dj_database_url
from biblelover.settings._base import *
import os

DEBUG = False

SECRET_KEY = get_env_variable('SECRET_KEY')

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(
    get_env_variable('DATABASE_URL'), conn_max_age=600)

ADMIN_EMAILS = [
    [get_env_variable("ADMIN_FULL_NAME"), get_env_variable("ADMIN_EMAIL_ADDRESS")]]

ADMINS = ADMIN_EMAILS

MANAGERS = ADMIN_EMAILS

ADMIN_URL = get_env_variable("ADMIN_URL")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
    "/app/assets/"
)
