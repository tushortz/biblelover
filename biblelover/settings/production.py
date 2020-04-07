from biblelover.settings.base import *
import dj_database_url

DEBUG = False

SECRET_KEY = get_env_variable('SECRET_KEY')

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(
    get_env_variable('DATABASE_URL'), conn_max_age=600)

admin_emails = [[get_env_variable("ADMIN_FULL_NAME"), get_env_variable("ADMIN_EMAIL_ADDRESS")]]

ADMINS = admin_emails

MANAGERS = admin_emails

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'biblelover/assets')
]