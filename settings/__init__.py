"""
An example settings module
"""

from __future__ import absolute_import, unicode_literals

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


# Development flags

DEBUG = True
BASE_DIR = dirname(dirname(abspath(__file__)))



# Application definition

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'default.db')  ,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
     'corsheaders',
    'customerdataapi',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root('customerdataapi', 'templates'), ],
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
CORS_ORIGIN_ALLOW_ALL=True
LOCALE_PATHS = [
    root('customerdataapi', 'conf', 'locale'),
]

ROOT_URLCONF = 'customerdataapi.urls'

SECRET_KEY = 'insecure-secret-key'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}


ALLOWED_HOSTS=['edx.developers.design','190.159.249.74','murmuring-cove-29205.herokuapp.com','127.0.0.1','192.168.1.102']



#URL_STREAM='http://streamerapi.finance.yahoo.com/streamer/1.0?s=^GDAXI,USD=X&o=BEI.F,SIE.F,PRA.F&k=l10,a00,b00,g00,h00&j=l10,a00,b00,g00,h00&r=0&marketid=us_market&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb'
#URL_STREAM='https://streamerapi.finance.yahoo.com/streamer/1.0?s=TSLA&s=^GDAXI,USD=X&o=^N225,LHS.F,JI4.F,EEX.F,HEI.F,CBK.F,PRE.F,NDX1.F&k=j10,c63,p43,l84,t53,v53&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb&mu=1&lang=en-US&region=US&localize=0'
URL_STREAM='https://streamerapi.finance.yahoo.com/streamer/1.0?s=TSLA&k=j10,c63,p43,l84,t53,v53&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb&mu=1&lang=en-US&region=US&localize=0'
#python manage.py  makemigrations && python manage.py migrate

#STATIC_ROOT = join(BASE_DIR, 'static')
STATICFILES_DIRS = ( join(BASE_DIR, "static"), )


STATIC_URL = '/static/'
