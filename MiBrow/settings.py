"""
Django settings for MiBrow project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nil+*bbvcfs&#c2mx0^#86ys5t+cx@44zq&8l!xho-d74get=d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'polls',
	'searchpage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MiBrow.urls'

WSGI_APPLICATION = 'MiBrow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'MiBrow',
		'USER':'root',
		'PASSWORD':'',
		'HOST':'localhost',
		'PORT':'',	
			
		
	}

}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True





#TEMPLATE_DIRS = (
#	os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),

STATIC_URL = '/static/'
"""
if DEBUG:
	MEDIA_URL = '/media/'
	STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static",
	MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static",
	STATICFILES_DIRS = (
		os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
	)	

"""
