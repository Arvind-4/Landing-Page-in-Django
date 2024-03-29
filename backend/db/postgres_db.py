from decouple import config

DJANGO_PG_DATABASE = config('DJANGO_PG_DATABASE', cast=str)
DJANGO_PG_USER = config('DJANGO_PG_USER', cast=str)
DJANGO_PG_PASSWORD = config('DJANGO_PG_PASSWORD', cast=str)
DJANGO_PG_HOST = config('DJANGO_PG_HOST', cast=str)
DJANGO_PG_PORT = config('DJANGO_PG_PORT', cast=str, default='')


DB_IS_AVAILABLE = all([
    DJANGO_PG_DATABASE,
    DJANGO_PG_USER,
    DJANGO_PG_PASSWORD,
    DJANGO_PG_HOST,
])

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DJANGO_PG_DATABASE,
            'USER': DJANGO_PG_USER,
            'PASSWORD': DJANGO_PG_PASSWORD,
            'HOST': DJANGO_PG_HOST,
            'PORT': DJANGO_PG_PORT,
        }
    }

    DATABASES['default']['CONN_MAX_AGE'] = None
    DATABASES['default']['ATOMIC_REQUESTS'] = True 