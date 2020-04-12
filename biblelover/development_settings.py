import os
from django.core.exceptions import ImproperlyConfigured
from biblelover.settings.base_setting import *


SECRET_KEY = "g%*g5pj-exx+4ad9092*st_@fttv!rl37m(m@32p622bg3h8p+"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(".", 'biblelover.db'),
        'OPTIONS': {
            'timeout': 20,
        }
    }
}

ADMIN_URL = 'admin/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = [
    '127.0.0.1',
]

STATIC_ROOT = os.path.join("BASE_DIR", 'assets')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]
