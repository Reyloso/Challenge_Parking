import os

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'parking_challenge',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

MEDIA_URL = '/files/'
MEDIA_ROOT = 'files/'

STATICFILES_DIRS = (
    os.path.join('static/'),
)