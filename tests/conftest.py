"""
Pytest configuration for label-studio-sso tests
"""

import os
import django
from django.conf import settings

# Configure Django settings for tests
if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'label_studio_sso',
        ],
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'label_studio_sso.middleware.ThingsFactoryAutoLoginMiddleware',
        ],
        AUTHENTICATION_BACKENDS=[
            'label_studio_sso.backends.ThingsFactoryJWTBackend',
            'django.contrib.auth.backends.ModelBackend',
        ],
        SECRET_KEY='test-secret-key-for-django',
        THINGS_FACTORY_JWT_SECRET='test-jwt-secret',
        USE_TZ=True,
    )
    django.setup()
