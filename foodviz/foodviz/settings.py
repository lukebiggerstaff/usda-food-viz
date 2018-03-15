import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Environment = {
    'DJANGO_DEBUG' : bool(int(os.environ.get("DJANGO_DEBUG"))),
    'DJANGO_SECRET' : os.environ.get("DJANGO_SECRET"),
    'DJANGO_DB_NAME' : os.environ.get("DJANGO_DB_NAME"),
    'DJANGO_DB_USER' : os.environ.get("DJANGO_DB_USER"),
    'DJANGO_DB_PASSWORD' : os.environ.get("DJANGO_DB_PASSWORD"),
    'DJANGO_DB_HOST' : os.environ.get("DJANGO_DB_HOST"),
    'DJANGO_DB_PORT' : os.environ.get("DJANGO_DB_PORT"),
    'DJANGO_SITENAME' : os.environ.get("DJANGO_SITENAME"),
}


DEBUG = Environment["DJANGO_DEBUG"]

SECRET_KEY = Environment["DJANGO_SECRET"]

ALLOWED_HOSTS = ["*" if Environment["DJANGO_DEBUG"] else Environment["DJANGO_SITENAME"]]

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': Environment['DJANGO_DB_NAME'],
                'USER': Environment['DJANGO_DB_USER'],
                'PASSWORD': Environment['DJANGO_DB_PASSWORD'],
                'HOST': Environment['DJANGO_DB_HOST'],
                'PORT': Environment['DJANGO_DB_PORT'],
    }
}

# webpack settings
WEBPACK_DEV = os.path.join(BASE_DIR, 'webpack-stats.dev.json')
WEBPACK_PROD = os.path.join(BASE_DIR, 'webpack-stats.prod.json')

WEBPACK_LOADER = {
    'DEFAULT' : {
        'BUNDLE_DIR_NAME' : 'bundles/',
        'STATS_FILE' : WEBPACK_DEV if DEBUG else WEBPACK_PROD,
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'search',
    'rest_framework',
    'webpack_loader',
]

# Configure streaming logging
LOGGING = {
        'version': 1,
    'handlers': {
        'console' : {
            'class' : 'logging.StreamHandler',
        },
    },
    'loggers' : {
        'django' : {
            'handlers' : ['console'],
            'level' : os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },

}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'foodviz.urls'

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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

