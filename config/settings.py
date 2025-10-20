in}$ python manage.py migrate
Traceback (most recent call last):
  File "/home/user/learning_platform/manage.py", line 11, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/user/learning_platform/manage.py", line 22, in <module>
    main()
  File "/home/user/learning_platform/manage.py", line 13, in main
    raise ImportError(
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
learningplatform-32266522:~/learning_platform{main}$ pip install django
pip is not installed, but available in the following packages, pick one to run it, Ctrl+C to cancel.
these 19 paths will be fetched (1.09 MiB download, 11.54 MiB unpacked):
  /nix/store/gnx2p695iqmlr0w88ccklbgwim6axcmb-ed-1.19
  /nix/store/v8p4q804sx0jjpds4xpk7sf64sy3jb1r-file-5.45
  /nix/store/rwrw7zjjw884w3myrjnhf78dq3zrmgsf-gnu-config-2023-09-19
  /nix/store/w9v3jmfwl6dc96l2p6k6c0lc6affyxi1-gnumake-4.4.1
  /nix/store/88gf3i3nis12h1z1mkrqjsycchgcqjzr-patch-2.7.6
  /nix/store/yf4fcxik258lrm0r4vxjv05wy1svd6i2-patchelf-0.15.0
  /nix/store/gfgwkpxhzkv0hk2a768g53iwnrznryl2-perl5.38.2-Class-Inspector-1.36
  /nix/store/2ais77ml9q90jssqqyvdlwwcb2y7gqsf-perl5.38.2-Env-Path-0.19
  /nix/store/vadb5l7pcz61s4wcnk7qma52m0mq3f4s-perl5.38.2-Exporter-Tiny-1.006002
  /nix/store/gfdq5wqf2dx4nch729x9jjy6w4c4x7vm-perl5.38.2-File-ShareDir-1.118
  /nix/store/a24aa057hk2xl22da1vgb67i4yaca66l-perl5.38.2-IO-Pty-1.16
  /nix/store/fs1aza5lk164n33k5h0gna85qwvj5jic-perl5.38.2-IO-Stty-0.04
  /nix/store/67c6g22igdzz6ylfxla1v7ial3j9n116-perl5.38.2-List-MoreUtils-0.430
  /nix/store/3jpg8y4wza1rbm0dfypkjvv46077r5r4-perl5.38.2-List-MoreUtils-XS-0.430
  /nix/store/0ayil13qspg3fdiadaf4yr698cgkaknl-perl5.38.2-Regexp-Common-2017060201
  /nix/store/p4j0daha8jr0m4v9zwglihxidnxdb51f-perl5.38.2-Regexp-IPv6-0.03
  /nix/store/5pzfkhmlfk6316ibf02s16wasjdq8wf0-perl5.38.2-cope-unstable-2015-01-29
  /nix/store/y6x85gyyndgbvzvdlz1y69gs1zxsa29f-stdenv-linux
  /nix/store/a4la4kzmq9kwqc71kf9lksx15pcq8wbg-update-autotools-gnu-config-scripts-hook
copying path '/nix/store/gfgwkpxhzkv0hk2a768g53iwnrznryl2-perl5.38.2-Class-Inspector-1.36' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/vadb5l7pcz61s4wcnk7qma52m0mq3f4s-perl5.38.2-Exporter-Tiny-1.006002' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/fs1aza5lk164n33k5h0gna85qwvj5jic-perl5.38.2-IO-Stty-0.04' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/0ayil13qspg3fdiadaf4yr698cgkaknl-perl5.38.2-Regexp-Common-2017060201' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/w9v3jmfwl6dc96l2p6k6c0lc6affyxi1-gnumake-4.4.1' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/p4j0daha8jr0m4v9zwglihxidnxdb51f-perl5.38.2-Regexp-IPv6-0.03' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/rwrw7zjjw884w3myrjnhf78dq3zrmgsf-gnu-config-2023-09-19' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/yf4fcxik258lrm0r4vxjv05wy1svd6i2-patchelf-0.15.0' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/gnx2p695iqmlr0w88ccklbgwim6axcmb-ed-1.19' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/2ais77ml9q90jssqqyvdlwwcb2y7gqsf-perl5.38.2-Env-Path-0.19' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/v8p4q804sx0jjpds4xpk7sf64sy3jb1r-file-5.45' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/a24aa057hk2xl22da1vgb67i4yaca66l-perl5.38.2-IO-Pty-1.16' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/3jpg8y4wza1rbm0dfypkjvv46077r5r4-perl5.38.2-List-MoreUtils-XS-0.430' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/a4la4kzmq9kwqc71kf9lksx15pcq8wbg-update-autotools-gnu-config-scripts-hook' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/88gf3i3nis12h1z1mkrqjsycchgcqjzr-patch-2.7.6' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/gfdq5wqf2dx4nch729x9jjy6w4c4x7vm-perl5.38.2-File-ShareDir-1.118' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/67c6g22igdzz6ylfxla1v7ial3j9n116-perl5.38.2-List-MoreUtils-0.430' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/y6x85gyyndgbvzvdlz1y69gs1zxsa29f-stdenv-linux' from 'https://cache.nixos.org' to 'local-overlay://'...
copying path '/nix/store/5pzfkhmlfk6316ibf02s16wasjdq8wf0-perl5.38.2-cope-unstable-2015-01-29' from 'https://cache.nixos.org' to 'local-overlay://'...
Executable not in $PATH: pip at /nix/store/5pzfkhmlfk6316ibf02s16wasjdq8wf0-perl5.38.2-cope-unstable-2015-01-29/bin/pip line 37.
To permanently add this package to your environment, please add pkgs.cope to the list of packages in your dev.nix file, then rebuild your environment'''
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
'''
import os
from datetime import timedelta
from pathlib import Path
from decouple import config, Csv
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', cast=Csv())

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
    'apps.courses',
    'apps.tests',
    'apps.core',
    'apps.teachers',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.NumericPasswordValidator'
        ),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=config('ACCESS_TOKEN_LIFETIME_MINUTES', cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=config('REFRESH_TOKEN_LIFETIME_DAYS', cast=int)),
}
