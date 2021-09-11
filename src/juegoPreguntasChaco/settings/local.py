import os

from .base import * 


DEBUG = True

ALLOWED_HOSTS = ['*']
# DB Elephant
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hdgrlqra',
        'USER': 'hdgrlqra',
        'PASSWORD': 'B2-hxfMfZSPEkFb64nu55fNgUSM3066p',
        'HOST': 'motty.db.elephantsql.com',
        'PORT': '5432',
    }
}