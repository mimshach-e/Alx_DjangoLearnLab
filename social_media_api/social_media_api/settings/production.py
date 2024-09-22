from .base import *
import os

# Set DEBUG to False in production
DEBUG = False

# Add your domain names to ALLOWED_HOSTS
ALLOWED_HOSTS = ['your-app-name.herokuapp.com', 'www.your-domain.com']

# Security settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Security settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # Redirect all HTTP connections to HTTPS
SESSION_COOKIE_SECURE = True  # Use secure cookies for sessions
CSRF_COOKIE_SECURE = True  # Use secure cookies for CSRF

# Database configuration (we'll use Heroku's PostgreSQL)
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Static files configuration (using WhiteNoise)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files configuration (you might want to use a service like Amazon S3 for this in a real production environment)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}