"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import LOGIN_URL, LOGOUT_URL,\
    LOGIN_REDIRECT_URL
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8!9e2!b%4-g02%15hs$i-h=4nnedh5724!!pj&9#a)vmr1xhbk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATICFILES_DIRS = (
                   os.path.join(BASE_DIR, 'static'),
                   )

TEMPLATE_DIRS = (
                os.path.join(BASE_DIR, 'templates'),
                )

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'marcador',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
                'NAME': 'MaestroMuebles',
                'ENGINE': 'sql_server.pyodbc',
                'HOST': '10.44.52.196',
                'USER': 'syspruebasmuebles',
                'PASSWORD': '4d6f709f8679e0759ca77b0a7c512e78',
                'PORT': '',
                'OPTIONS': {
                            'driver': 'SQL Server Native Client 11.0',
                            'MARS_Connection': True
                            }
                }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = 'mysite_login'
LOGOUT_URL = 'mysite_logout'
LOGIN_REDIRECT_URL = '/'