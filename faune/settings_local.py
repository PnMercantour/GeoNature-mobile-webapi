# Django settings for faune project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ID = 'default'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'appli_faune',                      # Or path to database file if using sqlite3.
        'USER': 'gisuser',                      # Not used with sqlite3.
        'PASSWORD': 'Rivirwaktim9',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },        
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        }        
    }
}


TOKEN = "666"

FAUNE_MOBILE_SOFT_PATH = "/home/sbe/tmp/"