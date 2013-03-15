# Django settings for faune project.
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASE_ID = 'default'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dbname',                      # Or path to database file if using sqlite3.
        'USER': 'dbuser',                      # Not used with sqlite3.
        'PASSWORD': 'userpassword',                  # Not used with sqlite3.
        'HOST': 'url',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2&amp;a^+yahrzn--_7f3-rr#-uu@6%93t)upl(mc0d$puonvj0yq)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'faune.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'faune.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'faune',
)

TEST_RUNNER = 'faune.faune_tests.DjangoTestSuiteRunner'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
            #'filters': ['require_debug_false'],
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
            'propagate': False, # this tells logger to send logging message
                                # to its parent (will send if set to True)
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

FAUNA_ID_ORGANISM = 2
FAUNA_ID_PROTOCOL = 140
FAUNA_ID_LOT = 4
MORTALITY_ID_PROTOCOL = 142
MORTALITY_ID_LOT = 15
            

TABLE_TAXA = 'contactfaune.v_nomade_taxons_faune'
TABLE_FAMILY = 'taxonomie.bib_familles'
TABLE_UNITY = 'contactfaune.v_nomade_unites_geo_cf'
TABLE_UNITY_GEOJSON = 'contactfaune.v_nomade_unites_geo_cf'
TABLE_TAXA_UNITY = 'contactfaune.cor_unite_taxon'
TABLE_CRITERION = 'contactfaune.v_nomade_criteres_cf'
TABLE_USER = 'contactfaune.v_nomade_observateurs_faune'
TABLE_STATEMENT = 'contactfaune.t_releves_cf'
TABLE_SHEET = 'contactfaune.t_fiches_cf'
TABLE_SHEET_ROLE = 'contactfaune.cor_role_fiche_cf'
TABLE_FAILED_JSON_FAUNA = 'synchronomade.erreurs_cf'
TABLE_FAILED_JSON_MORTALITY = 'synchronomade.erreurs_mortalite'
TABLE_CLASSES = 'taxonomie.bib_classes'



FAUNE_TABLE_INFOS =  {
    TABLE_FAILED_JSON_FAUNA: {
        'id_col': 'id',
        'select_col': 'id,json_date_import'
    },
    TABLE_FAILED_JSON_MORTALITY: {
        'id_col': 'id',
        'select_col': 'id,json_date_import'
    },
    TABLE_SHEET_ROLE: {
        #'id_col': 'id_role',
        'select_col': 'id_cf,id_role',
        'json_to_db_columns' : {
            'id_cf' : 'id_cf', 
            'observer_id' : 'id_role'    
        }        
    },    
    TABLE_STATEMENT: {
        'id_col': 'id_releve_cf',
        'select_col': 'id_releve_cf, id_cf, id_taxon, id_critere_cf, am, af, ai, na, sai, jeune, yearling, nom_taxon_saisi, commentaire, supprime, prelevement',
        'json_to_db_columns' : {
            'id_cf' : 'id_cf', 
            'id' : 'id_taxon',
            'criterion' : 'id_critere_cf',
            'adult_male' : 'am',
            'adult_female' : 'af',
            'adult' : 'ai',
            'not_adult' : 'na',
            'sex_age_unspecified' : 'sai',
            'young' : 'jeune',
            'yearling' : 'yearling',
            'name_entered' : 'nom_taxon_saisi',
            'comment' : 'commentaire',
            'supprime' : 'supprime',
            'sample' : 'prelevement'    
        }        
    },
    TABLE_SHEET: {
        'id_col': 'id_cf',
        'select_col': 'id_cf, dateobs, altitude_saisie, supprime, pdop, the_geom_2154, saisie_initiale, id_organisme, id_protocole, id_lot',
        'json_to_db_columns' : {
            'dateobs' : 'dateobs',
            'altitude' : 'altitude_saisie',
            'supprime' : 'supprime',
            'accuracy' : 'pdop',
            'geometry' : 'the_geom_2154',
            'initial_input' : 'saisie_initiale'
        }        
    },
    TABLE_TAXA: {
        'id_col': 'id_taxon',
        'json_name': 'taxa',
        'sqlite_name': 'taxa',
        'select_col': 'id_taxon, nom_latin, nom_francais, id_classe, denombrement, patrimonial, message, contactfaune',
        'db_to_json_columns' : {
            'id_taxon' : '_id',
            'cd_ref' : 'cd_ref',
            'nom_latin' : 'name',
            'nom_francais' : 'name_fr',
            'id_classe' : 'class_id',
            'denombrement' : 'number',
            'patrimonial' : 'patrimonial',
            'message' : 'message',
            'contactfaune' : 'cf'
        },
        'where_string' : 'contactfaune = TRUE'
    },
    
    TABLE_FAMILY: {
        'id_col': 'id_famille',
        'json_name': 'family',
        'sqlite_name': 'family',
        'select_col': 'id_famille, nom_famille',
        'db_to_json_columns' : {
            'id_famille' : 'id',
            'nom_famille' : 'name'
        }
    },
    TABLE_UNITY: {
        'id_col': 'id_unite_geo',
        'json_name': 'unity',
        'sqlite_name': 'unities',
        #'select_col': 'id_unite_geo, code_insee, commune',
        'select_col': 'id_unite_geo',
        'db_to_json_columns' : {
            'id_unite_geo' : '_id',
            'code_insee' : 'insee',
            'commune' : 'city'
        }        
    },
    TABLE_TAXA_UNITY: {
        'id_col': 'id_unite_geo',
        'json_name': 'taxa_unity',
        'sqlite_name': 'taxa_unities',
        'select_col': 'id_unite_geo, id_taxon, to_char(derniere_date,\'YYYY/MM/dd\') as derniere_date, couleur, nb_obs',
        'db_to_json_columns' : {
            'id_unite_geo' : 'unity_id',
            'id_taxon' : 'taxon_id',
            'derniere_date' : 'date',
            'couleur' : 'color',
            'nb_obs' : 'nb_obs'
        }        
    },
    TABLE_CRITERION: {
        'id_col': 'id_critere_cf',
        'json_name': 'criterion',
        'sqlite_name': 'criterion',
        'select_col': 'id_critere_cf, nom_critere_cf, tri_cf, id_classe',
        'db_to_json_columns' : {
            'id_critere_cf' : '_id',
            'nom_critere_cf' : 'name',
            'tri_cf' : 'sort',
            'id_classe' : 'class_id'
        }        
    },
    TABLE_USER: {
        'id_col': 'id_role',
        'json_name': 'user',
        'sqlite_name': 'observers',
        'select_col': 'id_role, nom_role, prenom_role',
        'db_to_json_columns' : {
            'id_role' : '_id',
            'identifiant' : 'ident',
            'nom_role' : 'lastname',
            'prenom_role' : 'firstname'
        }        
    },
    
    TABLE_CLASSES: {
        'id_col': 'id_classe',
        'json_name': 'classes',
        'sqlite_name': 'classes',
        'select_col': 'id_classe, nom_classe, desc_classe',
        'db_to_json_columns' : {
            'id_classe' : '_id',
            'nom_classe' : 'name',
            'desc_classe' : 'description'
        }        
    }
}

FAUNE_TABLE_INFOS_GEOJSON =  {
    TABLE_UNITY_GEOJSON: {
        'id_col': 'id_unite_geo',
        'json_name': 'unity_geojson',
        'select_col': 'id_unite_geo, ST_AsText(ST_SnapToGrid(transform(the_geom,4326),0.00001)) as geom',
        #'select_col': 'id_unite_geo, ST_AsText(ST_SnapToGrid(transform(the_geom,4326),0.001)) as geom',
        'db_to_json_columns' : {
            'id_unite_geo' : 'id',
            'code_insee' : 'insee',
            'commune' : 'city',
            'geom': 'geometry'
        }        
    }
}
    
FAUNE_MOBILE_SQLITE_SAMPLE = os.path.join(PROJECT_ROOT_PATH, "data.db.sample")

FAUNE_MOBILE_SQLITE_CREATE_QUERY = (
    'CREATE TABLE IF NOT EXISTS observers (_id INTEGER, ident TEXT, lastname TEXT, firstname TEXT)',
    'CREATE TABLE IF NOT EXISTS taxa_unities (unity_id INTEGER, taxon_id INTEGER, date TEXT, color TEXT, nb_obs INTEGER)',
    'CREATE TABLE IF NOT EXISTS taxa (_id INTEGER, name TEXT, name_fr TEXT, class_id INTEGER, number INTEGER, patrimonial INTEGER, message TEXT, cf INTEGER)',
    'CREATE TABLE IF NOT EXISTS criterion (_id INTEGER, name TEXT, sort INTEGER, class_id INTEGER)',
    'CREATE TABLE IF NOT EXISTS android_metadata (locale TEXT DEFAULT "en_US")'
)


FAUNE_MOBILE_SQLITE_EXTRA_SQL = (
    'INSERT INTO android_metadata VALUES ("en_US")',
)

from settings_local import *