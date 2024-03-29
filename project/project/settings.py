"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j&n112!cwpd!zwcy&vwn!ge7$1injrs*q+9jqdp-heyty*du+@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'newsapp.apps.NewsappConfig',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "Harryckti"
EMAIL_HOST_PASSWORD = "vxoznkylzsnizkcq"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "Harryckti@yandex.ru"

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'formbug': {
            'format': '%(asctime)s %(levelname)s %(message)s', #все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения
        },
        'formwarning': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s', #Для сообщений WARNING и выше дополнительно должен выводиться путь к источнику события (используется аргумент pathname в форматировании)
        },
        'formerrorcritical': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s', #для сообщений ERROR и CRITICAL еще должен выводить стэк ошибки (аргумент exc_info)
        },
        'forminfo': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s', #с указанием времени, уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue', #в консоль сообщения отправляются только при DEBUG = True
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse', #на почту и в файл general.log — только при DEBUG = False
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG', #В консоль должны выводиться все сообщения уровня DEBUG и выше
            'filters': ['require_debug_true'], #в консоль сообщения отправляются только при DEBUG = True
            'class': 'logging.StreamHandler',
            'formatter': 'formbug', #все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'formwarning', #Для сообщений WARNING и выше дополнительно должен выводиться путь к источнику события (используется аргумент pathname в форматировании)
        },
        'console_errors_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'formerrorcritical', #еще должен выводить стэк ошибки (аргумент exc_info)
        },
        'mail_admins': {
            'level': 'ERROR', #На почту должны отправляться сообщения уровней ERROR
            'filters': ['require_debug_false'], #а почту и в файл general.log — только при DEBUG = False
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'formwarning', #по формату, как в errors.log, но без стэка ошибок.
        },
        'general': {
            'level': 'INFO', #В файл general.log должны выводиться сообщения уровня INFO
            'filters': ['require_debug_false'], #а почту и в файл general.log — только при DEBUG = False
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'forminfo', #с указанием времени, уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение
        },
        'errors': {
            'level': 'ERROR', #В файл errors.log должны выводиться сообщения только уровня ERROR и CRITICAL
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'formerrorcritical', #указывается время, уровень логирования, само сообщение, путь к источнику сообщения и стэк ошибки
        },
        'security': {
            'level': 'WARNING', #В файл security.log должны попадать только сообщения, связанные с безопасностью
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'forminfo', #предполагает время, уровень логирования, модуль и сообщение
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_errors_critical', 'general'], #первый пункт задания + второй
            'level': 'DEBUG',
            'propagate': True, #все сообщения уровня DEBUG и выше
        },
        'django.request': {
            'handlers': ['mail_admins', 'errors'], #пятый и третий пункты задания
            'propagate': True, #уровней ERROR и выше
        },
        'django.server': {
            'handlers': ['mail_admins', 'errors'], #пятый и третий пункты задания
            'propagate': True, #уровней ERROR и выше
        },
        'django.template': {
            'handlers': ['errors'], #третий пункт задания
            'propagate': True, #только уровня ERROR и CRITICAL
        },
        'django.db.backends': {
            'handlers': ['errors'], #третий пункт задания
            'propagate': True, #только уровня ERROR и CRITICAL
        },
        'django.security': {
            'handlers': ['security'], #четвертый пункт задания
            'propagate': False, #В файл security.log должны попадать только сообщения, связанные с безопасностью
        },
    },
}