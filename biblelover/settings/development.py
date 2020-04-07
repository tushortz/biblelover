from biblelover.settings.base import *
import os
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DEBUG = False

SECRET_KEY = "g%*g5pj-exx+4ad9092*st_@fttv!rl37m(m@32p622bg3h8p+"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'biblelover.db'),
        'OPTIONS': {
            'timeout': 20,
        }
    }
}