"""
Django settings for SunmTools project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys, dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG_PRO", 1))
if DEBUG:
    SECRET_KEY = "5)(5ih(u#0a!i35sz$pk=!4ikjt3-+%d76u@i)utb_pv5wy@sa"
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'tools',
    #         'USER': 'sky',
    #         'PASSWORD': 'password123',
    #         'HOST': '192.168.8.8',
    #         'PORT': '5432',
    #     },
    # }
    DATABASES = {
        "default": dj_database_url.config(
            default="postgres://sky:password123@192.168.8.8:5432/tools",
            conn_max_age=600,
        )
    }
    # get cfg from local file
    import local_cfg

    WECHATAPI = local_cfg.WECHATAPI
    WFAPI = local_cfg.WFAPI
else:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ.get("DATABASE_URL"), conn_max_age=600
        )
    }
    WECHATAPI = {
        "ID": os.environ.get("WECHAT_ID"),
        "SECRET": os.environ.get("WECHAT_SECRET"),
        "TOCKEN": os.environ.get("WECHAT_TOCKEN"),
    }
    WFAPI = {
        "BASE_URL": "https://api.richasy.cn",
        "ClientId": os.environ.get("WF_CID"),
        "ClientSecret": os.environ.get("WF_CS"),
    }

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "server.apps.ServerConfig",
    "blog.apps.BlogConfig",
    "notice.apps.NoticeConfig",
    "note.apps.NoteConfig",
    "warframe.apps.WarframeConfig",
    "wechat.apps.WechatConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "SunmTools.urls"
AUTH_USER_MODEL = "server.UserInfo"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "SunmTools.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATICFILES_DIRS = ()
