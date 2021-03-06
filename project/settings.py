"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.0b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import dj_database_url
import dj_email_url
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOTENV_PATH = os.path.join(BASE_DIR, '.env')

if os.path.exists(DOTENV_PATH):
    load_dotenv(DOTENV_PATH)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEBUG' in os.environ

if DEBUG:
    os.environ.setdefault(
        'SECRET_KEY',
        'I am an insecure secret key intended ONLY for dev/testing.'
    )
    os.environ.setdefault(
        'EMAIL_URL',
        os.environ.get('DEFAULT_DEBUG_EMAIL_URL', 'console:')
    )
    os.environ.setdefault('DEFAULT_FROM_EMAIL', 'noreply@localhost')
    os.environ.setdefault('SERVER_EMAIL', 'system@localhost')
    os.environ.setdefault('UAA_CLIENT_ID', 'fake-client-id')
    os.environ.setdefault('UAA_CLIENT_SECRET', 'fake-client-secret')

email_config = dj_email_url.config()
# Sets a number of settings values, as described at
# https://github.com/migonzalvar/dj-email-url
vars().update(email_config)

DEFAULT_FROM_EMAIL = os.environ['DEFAULT_FROM_EMAIL']
SERVER_EMAIL = os.environ['SERVER_EMAIL']

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_extensions',
    'marketplace.apps.MarketplaceConfig',
    'uaa_client',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'uaa_client.middleware.UaaRefreshMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'project.jinja2.environment',
        }
    }
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_URL = 'uaa_client:login'

UAA_APPROVED_DOMAINS = [
    'gsa.gov',
]

AUTHENTICATION_BACKENDS = [
    'uaa_client.authentication.UaaBackend',
]

UAA_AUTH_URL = 'https://login.fr.cloud.gov/oauth/authorize'

UAA_TOKEN_URL = 'https://uaa.fr.cloud.gov/oauth/token'

if DEBUG:
    UAA_AUTH_URL = UAA_TOKEN_URL = 'fake:'

UAA_CLIENT_ID = os.environ['UAA_CLIENT_ID']

UAA_CLIENT_SECRET = os.environ['UAA_CLIENT_SECRET']

LOGIN_REDIRECT_URL = '/'
