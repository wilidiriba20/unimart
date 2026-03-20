import os
from pathlib import Path

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-*0h_@ee)!2k^x0l$a-pp7bel4(ik_9&aiq*l=hsf8opr=&by+b'
DEBUG = True
ALLOWED_HOSTS = []

# Custom User
AUTH_USER_MODEL = 'accounts.User'

# ===================================================================
# 🔹 APPLICATION DEFINITION
# ===================================================================
INSTALLED_APPS = [
  
    'jazzmin',   
    'django.contrib.admin',    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'products',
    'messaging',
    'dashbord', 
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

AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailBackend',  # custom backend
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'unimart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'unimart.wsgi.application'

# ===================================================================
# DATABASE
# ===================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===================================================================
# PASSWORD VALIDATION
# ===================================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ===================================================================
# INTERNATIONALIZATION
# ===================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===================================================================
# STATIC & MEDIA FILES
# ===================================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

JAZZMIN_SETTINGS = {
    "site_title": "Unimart Admin",
    "site_header": "Unimart Admin",
    "site_brand": "Unimart Admin",               # hide text
    "welcome_sign": "Welcome to Unimart Admin",
    "custom_css": "css/jazzmin_custom.css",
    "site_logo": "images/logo.png", # path relative to static
              # width in pixels
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",  # or any Bootswatch theme
}