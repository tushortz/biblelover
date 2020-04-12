import os
from django.core.exceptions import ImproperlyConfigured
from biblelover.settings._all_auth_settings import *
from biblelover.settings._markdownify_setting import *
import dj_database_url


def get_env_variable(var_name):
    """
    return environment variable otherwise throws
    `django.core.exceptions.ImproperlyConfigured` error
    """

    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'background_task',
    'django.contrib.sites',

    # Local
    'base',
    'bible',
    'note',
    'preference',

    # 3rd party
    'markdownify',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

ROOT_URLCONF = 'biblelover.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'biblelover.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_REDIRECT_URL = '/dashboard/'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

DEBUG = False

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PAGINATE_COUNT = 50

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

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

STATIC_URL = '/assets/'

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'biblelover/assets'),
]
