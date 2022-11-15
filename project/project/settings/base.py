"""
Django config for project project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of config and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


from django.urls import reverse_lazy
from pathlib import Path
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env_file = Path(__file__).resolve().parent / "local.env"
if env_file.exists():
    environ.Env.read_env(str(env_file))

# STATICFILES_DIRS = [str(BASE_DIR / "static"),  str(BASE_DIR.parent / "site" / "static")]
# MEDIA_ROOT = str(BASE_DIR / "media")
# MEDIA_URL = "/media/"

# Quick-start development config - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "django_dramatiq",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_tables2',
    'rest_framework',
    'rest_framework.authtoken',
    'account_app',
    'image_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'SERIALIZERS' : {

    },
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
}

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


CELERY_BROKER_URL = "pyamqp://localhost:5672"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_IGNORE_RESULT = True
CELERY_DISABLE_RATE_LIMITS = False
CELERY_HIJACK_ROOT_LOGGER = False

DRAMATIQ_BROKER = {
    "BROKER": env("MESSAGE_BROKER_ENGINE", default="dramatiq.brokers.rabbitmq.RabbitmqBroker"),
    "OPTIONS": {
        "url": env("MESSAGE_BROKER_URL", default="amqp://localhost:5672"),
    },
    "MIDDLEWARE": [
        "dramatiq.middleware.Prometheus",
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        "dramatiq.middleware.Callbacks",
        "dramatiq.middleware.Retries",
        "django_dramatiq.middleware.DbConnectionsMiddleware",
        "django_dramatiq.middleware.AdminMiddleware",
    ]
}

DRAMATIQ_AUTODISCOVER_MODULES = ["tasks",]

# DATABASES = {
#     'default': {
#         'ENGINE': env('SQL_ENGINE', default='django.db.backends.sqlite3'),
#         'NAME': env('SQL_DATABASE', default=str(BASE_DIR / 'db.sqlite3')),
#         "USER": env("SQL_USER", default="user"),
#         "PASSWORD": env("SQL_PASSWORD", default="password"),
#         "HOST": env("SQL_HOST", default="localhost"),
#         "PORT": env("SQL_PORT", default="5432"),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

CRISPY_TEMPLATE_PACK = 'bootstrap4'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = str(BASE_DIR / "static")
MEDIA_ROOT = str(BASE_DIR / "media")
LOGIN_URL = reverse_lazy("login")
