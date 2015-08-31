import os

# Django settings for helloworld project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Bob', 'bob@example.com'),
)

path_components = os.path.dirname(__file__).split('/')
PROJECT_DIR = '/'.join(path_components[:-1]) + '/'

BASE_URL = 'http://127.0.0.1:8000/'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'helloworld.sqlite',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = PROJECT_DIR + 'media/'

MEDIA_URL = BASE_URL + 'media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_URL = BASE_URL + 'static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '!px^n5(#4i9_(o65st)xju%u2(y#(3=0*=o%$^(&po(ey88yiv'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'helloworld.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'static')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helloworld',
)