"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETTINGS_PATH = os.path.join(BASE_DIR + '/settings.json')
with open(SETTINGS_PATH) as f:
  settings = json.loads(f.read())

# SECRET_KEY_PATH = os.path.join(BASE_DIR + '/secret_key.json')
# with open(SECRET_KEY_PATH) as f:
#   secrets = json.loads(f.read())

SECRET_KEY = settings['secret_key']
KEY_PATH = os.path.join(BASE_DIR + '/key.json')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', settings['debug']))

if settings['mode'] == 'dev':
  ALLOWED_HOSTS = ['*']
else:
  ALLOWED_HOSTS = ['devpunch.xyz']

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  'django.contrib.sites',
  'django.contrib.sitemaps',

  'myblog',
  'myblog.templatetags',

  'category.apps.CategoryConfig',
  'post.apps.PostConfig',

  'ckeditor',
  'ckeditor_uploader',
  'disqus',
  'taggit',
  'taggit_templatetags2',
  'hitcount',
  'mptt',
  'sass_processor',
]


MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': TEMPLATE_DIRS,
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

WSGI_APPLICATION = 'myblog.wsgi.application'

DATABASES = {
  'default': json.loads(open(KEY_PATH).read())
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static2')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

SITE_ID = 1
DISQUS_WEBSITE_SHORTNAME = 'pythonweb-4'

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'extraPlugins': 'codesnippet',
    },
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# SASS_PROCESSOR_ENABLED = True

# COMPRESS_PRECOMPILERS = (
#   ('text/x-scss', 'django_libsass.SassCompiler'),
# )
#
# COMPRESS_OFFLINE = True
# LIBSASS_OUTPUT_STYLE = 'compressed'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# SASS_ROOT = STATIC_ROOT
# SASS_PROCESSOR_ROOT = STATIC_ROOT
# SASS_PROCESSOR_ENABLED = True
