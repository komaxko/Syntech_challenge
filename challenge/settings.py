import os
from datetime import timedelta
from configurations import Configuration


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third party apps
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authentication
        'django_filters',            # for filtering rest endpoints
        'corsheaders',               # cors for FE

        # Project apps
        'base',
        'tables',
        'orders',
    ]
    DATABASES = {
        'default': {}
    }

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]

    ROOT_URLCONF = 'challenge.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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

    WSGI_APPLICATION = 'challenge.wsgi.application'

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

    # Static files (CSS, JavaScript, Images)
    STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(BASE_DIR), 'static'))
    STATICFILES_DIRS = []
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=7)
    }

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],

        'DEFAULT_RENDERER_CLASSES': (
            'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
            'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        ),

        'DEFAULT_PARSER_CLASSES': (
            'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        ),
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '%(created)f %(asctime)s %(levelname)s %(process)d %(name)s.%(funcName)s:%(lineno)d %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'json'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'json',
                'filename': f'{BASE_DIR}/logging.log',
            },

        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
                'propagate': True,
            },
            'django': {
                'handlers': ['default'],
                'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
                'propagate': True,
            },
        },
    }

    REDIS_HOSTNAME = os.getenv('REDIS_HOSTNAME')
    REDIS_PORT = os.getenv('REDIS_PORT')
    REDIS_DB_NUMBER = os.getenv('REDIS_DB_NUMBER')
    REDIS_URL = "redis://{}:{}/{}".format(REDIS_HOSTNAME, REDIS_PORT, REDIS_DB_NUMBER)

    CACHES = {
        "default": {
            "BACKEND": "redis_cache.RedisCache",
            "LOCATION": REDIS_URL,

        }
    }

    EMAIL_SENDER = os.getenv('EMAIL_SENDER')


class Local(Base):
    SECRET_KEY = Base.SECRET_KEY
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'db',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'db',
            'PORT': '',
        }
    }

    # Cors
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = [
        "http://127.0.0.1",
        "http://localhost",
    ]
    CORS_ALLOW_HEADERS = [
        'accept',
        'accept-encoding',
        'authorization',
        'content-type',
        'dnt',
        'origin',
        'user-agent',
        'x-csrftoken',
        'x-requested-with',
        'siteId'
    ]
    LOGGING = {}


class Test(Base):
    DEBUG = True
    LOGGING = {}
    SECRET_KEY = Base.SECRET_KEY
    INSTALLED_APPS = Base.INSTALLED_APPS
    INSTALLED_APPS += (
        'django_nose',  # for test coverage
    )

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'db',
            'USER': 'user',
            'PASSWORD': 'password',
            'HOST': 'db',
            'PORT': '',
        }
    }

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        '--with-coverage',
        '--cover-erase',
        '--cover-inclusive',
        '--cover-package=orders,tables',
    ]
