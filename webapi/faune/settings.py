# -*- coding: utf-8 -*-
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
INV_ID_LOT = 14
INV_ID_PROTOCOL = 141

FLORA_ID_ORGANISM = 2
FLORA_FREQUENCY_ESTIMATION = 'S'
FLORA_FREQUENCY_TRANSECT = 'N'

FLORA_COUNTING_NONE = 9
FLORA_COUTING_SAMPLING = 2
FLORA_COUTING_EXHAUSTIVE = 1

DB_FAUNA = 'fauna'
DB_INV = 'inv'
DB_FLORA = 'flora'
            
TABLE_FAUNA_TAXA = 'contactfaune.v_nomade_taxons_faune'
TABLE_FAUNA_FAMILY = 'taxonomie.bib_familles'
TABLE_FAUNA_UNITY = 'contactfaune.v_nomade_unites_geo_cf'
TABLE_FAUNA_UNITY_GEOJSON = 'contactfaune.v_nomade_unites_geo_cf'
TABLE_FAUNA_TAXA_UNITY = 'contactfaune.cor_unite_taxon'
TABLE_FAUNA_CRITERION = 'contactfaune.v_nomade_criteres_cf'
TABLE_FAUNA_USER = 'contactfaune.v_nomade_observateurs_faune'
TABLE_FAUNA_STATEMENT = 'contactfaune.t_releves_cf'
TABLE_FAUNA_SHEET = 'contactfaune.t_fiches_cf'
TABLE_FAUNA_SHEET_ROLE = 'contactfaune.cor_role_fiche_cf'
TABLE_FAILED_JSON_FAUNA = 'synchronomade.erreurs_cf'
TABLE_FAILED_JSON_MORTALITY = 'synchronomade.erreurs_mortalite'
TABLE_FAUNA_CLASSES = 'taxonomie.bib_classes'


TABLE_INV_TAXA = 'contactinv.v_nomade_taxons_inv'
TABLE_INV_FAMILY = 'taxonomie.bib_familles'
TABLE_INV_UNITY = 'contactinv.v_nomade_unites_geo_inv'
TABLE_INV_UNITY_GEOJSON = 'contactinv.v_nomade_unites_geo_inv'
TABLE_INV_TAXA_UNITY = 'contactinv.cor_unite_taxon_inv'
TABLE_INV_CRITERION = 'contactinv.v_nomade_criteres_inv'
TABLE_INV_USER = 'contactinv.v_nomade_observateurs_inv'
TABLE_INV_STATEMENT = 'contactinv.t_releves_inv'
TABLE_INV_SHEET = 'contactinv.t_fiches_inv'
TABLE_INV_SHEET_ROLE = 'contactinv.cor_role_fiche_inv'
TABLE_INV_ENVIRONEMENTS = 'contactinv.v_nomade_milieux_inv'
TABLE_FAILED_JSON_INV = 'synchronomade.erreurs_inv'
TABLE_INV_CLASSES = 'taxonomie.bib_classes'


TABLE_FLORA_TAXA = 'florepatri.v_mobile_taxons_fp'
TABLE_FLORA_FAMILY = 'taxonomie.bib_familles'
TABLE_FLORA_USER = 'florepatri.v_mobile_observateurs_fp'
TABLE_FLORA_COR_ZP_OBS = 'florepatri.cor_zp_obs'
TABLE_FLORA_T_APRESENCE = 'florepatri.t_apresence'
TABLE_FLORA_T_ZPROSPECTION = 'florepatri.t_zprospection'
TABLE_FLORA_COR_AP_PERTURB = 'florepatri.cor_ap_perturb'
TABLE_FLORA_COR_AP_PHYSIONOMIE = 'florepatri.cor_ap_physionomie'
TABLE_FAILED_JSON_FLORA = 'synchronomade.erreurs_flora'
TABLE_FLORA_CLASSES = 'taxonomie.bib_classes'
TABLE_FLORA_INCLINES = 'florepatri.v_mobile_pentes'
TABLE_FLORA_DISTURBANCES = 'florepatri.v_mobile_perturbations'
TABLE_FLORA_PHENOLOGY = 'florepatri.v_mobile_phenologies'
TABLE_FLORA_PHYSIOGNOMY = 'florepatri.v_mobile_physionomies'
TABLE_FLORA_VISU_FP = 'florepatri.v_mobile_visu_zp'
TABLE_FLORA_SEARCH = 'public.v_mobile_recherche'

TABLE_USERS = 'utilisateurs.v_nomade_observateurs_all'

# GLOBAL -------------------------------------------------------------------
GLOBAL_TABLE_INFOS =  {
    'database_id': 'fauna',
    TABLE_USERS: {
        'id_col': 'id_role',
        'json_name': 'user',
        'sqlite_name': 'observers',
        'select_col': 'id_role, nom_role, prenom_role, string_agg(mode, \',\') as mode',
        'db_to_json_columns' : {
            'id_role' : '_id',
            'identifiant' : 'ident',
            'nom_role' : 'lastname',
            'prenom_role' : 'firstname',
            'mode' : 'mode',
        },
        'groupby_string' : 'id_role, nom_role, prenom_role'
    }
}


# FAUNA -------------------------------------------------------------------
FAUNE_TABLE_INFOS =  {
    'database_id': 'fauna',
    TABLE_FAILED_JSON_FAUNA: {
        'id_col': 'id',
        'select_col': 'id,json_date_import'
    },
    TABLE_FAILED_JSON_MORTALITY: {
        'id_col': 'id',
        'select_col': 'id,json_date_import'
    },
    TABLE_FAUNA_SHEET_ROLE: {
        #'id_col': 'id_role',
        'select_col': 'id_cf,id_role',
        'json_to_db_columns' : {
            'id_cf' : 'id_cf', 
            'observer_id' : 'id_role'    
        }        
    },    
    TABLE_FAUNA_STATEMENT: {
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
    TABLE_FAUNA_SHEET: {
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
    TABLE_FAUNA_TAXA: {
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
        #'where_string' : 'contactfaune = TRUE'
    },
    
    TABLE_FAUNA_FAMILY: {
        'id_col': 'id_famille',
        'json_name': 'family',
        'sqlite_name': 'family',
        'select_col': 'id_famille, nom_famille',
        'db_to_json_columns' : {
            'id_famille' : 'id',
            'nom_famille' : 'name'
        }
    },
    TABLE_FAUNA_UNITY: {
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
    TABLE_FAUNA_TAXA_UNITY: {
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
    TABLE_FAUNA_CRITERION: {
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
    TABLE_FAUNA_USER: {
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
    
    TABLE_FAUNA_CLASSES: {
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


# INV -------------------------------------------------------------------
INV_TABLE_INFOS =  {
    'database_id': 'inv',
    TABLE_FAILED_JSON_INV: {
        'id_col': 'id',
        'select_col': 'id,json_date_import'
    },
    TABLE_INV_SHEET_ROLE: {
        'select_col': 'id_inv,id_role',
        'json_to_db_columns' : {
            'id_inv' : 'id_inv', 
            'observer_id' : 'id_role'    
        }        
    },    
    TABLE_INV_STATEMENT: {
        'id_col': 'id_releve_inv',
        'select_col': 'id_releve_inv, id_inv, id_taxon, id_critere_inv, am, af, ai, na, nom_taxon_saisi, commentaire, supprime, prelevement',
        'json_to_db_columns' : {
            'id_inv' : 'id_inv', 
            'id' : 'id_taxon',
            'criterion' : 'id_critere_inv',
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
    TABLE_INV_SHEET: {
        'id_col': 'id_inv',
        'select_col': 'id_inv, dateobs, heure, altitude_saisie, supprime, pdop, the_geom_2154, saisie_initiale, id_organisme, id_protocole, id_lot, id_milieu_inv',
        'json_to_db_columns' : {
            'dateobs' : 'dateobs',
            'altitude' : 'altitude_saisie',
            'supprime' : 'supprime',
            'accuracy' : 'pdop',
            'geometry' : 'the_geom_2154',
            'initial_input' : 'saisie_initiale',
            'environment' : 'id_milieu_inv',
            'heure' : 'heure'
        }        
    },
    TABLE_INV_TAXA: {
        'id_col': 'id_taxon',
        'json_name': 'taxa',
        'sqlite_name': 'taxa',
        'select_col': 'id_taxon, nom_latin, nom_francais, id_classe, patrimonial, message',
        'db_to_json_columns' : {
            'id_taxon' : '_id',
            'cd_ref' : 'cd_ref',
            'nom_latin' : 'name',
            'nom_francais' : 'name_fr',
            'id_classe' : 'class_id',
            'patrimonial' : 'patrimonial',
            'message' : 'message'
        },
        #'where_string' : 'contactfaune = TRUE'
    },
    
    TABLE_INV_FAMILY: {
        'id_col': 'id_famille',
        'json_name': 'family',
        'sqlite_name': 'family',
        'select_col': 'id_famille, nom_famille',
        'db_to_json_columns' : {
            'id_famille' : 'id',
            'nom_famille' : 'name'
        }
    },
    TABLE_INV_UNITY: {
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
    TABLE_INV_TAXA_UNITY: {
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
    TABLE_INV_CRITERION: {
        'id_col': 'id_critere_inv',
        'json_name': 'criterion',
        'sqlite_name': 'criterion',
        'select_col': 'id_critere_inv, nom_critere_inv, tri_inv',
        'db_to_json_columns' : {
            'id_critere_inv' : '_id',
            'nom_critere_inv' : 'name',
            'tri_inv' : 'sort'
        }        
    },
    TABLE_INV_USER: {
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
    
    TABLE_INV_CLASSES: {
        'id_col': 'id_classe',
        'json_name': 'classes',
        'sqlite_name': 'classes',
        'select_col': 'id_classe, nom_classe, desc_classe',
        'db_to_json_columns' : {
            'id_classe' : '_id',
            'nom_classe' : 'name',
            'desc_classe' : 'description'
        }        
    },
    
    TABLE_INV_ENVIRONEMENTS: {
        'id_col': 'id_milieu_inv',
        'json_name': 'environments',
        'sqlite_name': 'environments',
        'select_col': 'id_milieu_inv, nom_milieu_inv',
        'db_to_json_columns' : {
            'id_milieu_inv' : '_id',
            'nom_milieu_inv' : 'name'
        }        
    },
    
}

# FLORA -------------------------------------------------------------------
FLORA_TABLE_INFOS =  {
    'database_id': 'flora',
    TABLE_FAILED_JSON_FLORA: {
        'id_col': 'id',
        'select_col': 'id,json_date_import'
    },
    
    TABLE_FLORA_T_APRESENCE: {
        'id_col': 'indexap',
        'json_name': 't_apresence',
        'sqlite_name': 't_apresence',
        'select_col': 'indexap',
        'json_to_db_columns' : {
            'id' : 'indexap',
            'phenology' : 'codepheno',
            'indexzp' : 'id',
            'computed_area' : 'surfaceap',
            'id_frequence_methodo_new' : 'id_frequence_methodo_new',
            'frequenceap' : 'frequenceap',
            'geometry' : 'the_geom_2154',
            'nb_transects_frequence' : 'nb_transects_frequence',
            'nb_points_frequence' : 'nb_points_frequence',
            'nb_contacts_frequence' : 'nb_contacts_frequence',
            'id_comptage_methodo' : 'id_comptage_methodo',
            'nb_placettes_comptage' : 'nb_placettes_comptage',
            'surface_placette_comptage' : 'surface_placette_comptage',
            'longueur_pas' : 'longueur_pas',
            'comment' : 'remarques',
            'supprime' : 'supprime',
            'effectif_placettes_steriles' : 'effectif_placettes_steriles',
            'effectif_placettes_fertiles' : 'effectif_placettes_fertiles',
            'total_steriles' : 'total_steriles',
            'total_fertiles' : 'total_fertiles'
        },
    },
   
    TABLE_FLORA_T_ZPROSPECTION: {
        'id_col': 'indexzp',
        'json_name': 't_zprospection',
        'sqlite_name': 't_zprospection',
        'select_col': '',
        'json_to_db_columns' : {
            'id' : 'indexzp',
            'geometry' : 'the_geom_2154',
            'id_taxon' : 'cd_nom',
            'initial_input' : 'saisie_initiale',
            'name_entered' : 'taxon_saisi',
            'id_organisme' : 'id_organisme',
            'srid_dessin' : 'srid_dessin',
            'supprime' : 'supprime',
            'dateobs' : 'dateobs'
        },
    },

    TABLE_FLORA_COR_ZP_OBS: {
        'id_col': 'indexzp',
        'json_name': 'cor_zp_obs',
        'sqlite_name': 'cor_zp_obs',
        'select_col': 'indexzp, codeobs',
        'json_to_db_columns' : {
            'id' : '_id',
            'indexzp' : 'indexzp',
            'codeobs' : 'codeobs'
        },
    },
    
    TABLE_FLORA_COR_AP_PERTURB: {
        'id_col': 'indexap',
        'json_name': 'cor_ap_perturb',
        'sqlite_name': 'cor_ap_perturb',
        'select_col': 'indexap, codeper',
        'json_to_db_columns' : {
            'id' : '_id',
            'indexap' : 'indexap',
            'codeper' : 'codeper'
        },
    },
    
    TABLE_FLORA_COR_AP_PHYSIONOMIE: {
        'id_col': 'indexap',
        'json_name': 'cor_zp_obs',
        'sqlite_name': 'cor_zp_obs',
        'select_col': 'indexap, id_physionomie',
        'json_to_db_columns' : {
            'id' : '_id',
            'indexap' : 'indexap',
            'id_physionomie' : 'id_physionomie'
        },        
    },
    
    TABLE_FLORA_TAXA: {
        'id_col': 'num_nomenclatural',
        'json_name': 'taxa',
        'sqlite_name': 'taxa',
        'select_col': 'cd_nom, nom_latin, nom_francais',
        'db_to_json_columns' : {
            'cd_nom' : '_id',
            'nom_latin' : 'name',
            'nom_francais' : 'name_fr'
        },
        #'where_string' : 'contactfaune = TRUE'
    },
    
    TABLE_FLORA_FAMILY: {
        'id_col': 'id_famille',
        'json_name': 'family',
        'sqlite_name': 'family',
        'select_col': 'id_famille, nom_famille',
        'db_to_json_columns' : {
            'id_famille' : 'id',
            'nom_famille' : 'name'
        }
    },
    TABLE_FLORA_USER: {
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
    
    TABLE_FLORA_CLASSES: {
        'id_col': 'id_classe',
        'json_name': 'classes',
        'sqlite_name': 'classes',
        'select_col': 'id_classe, nom_classe, desc_classe',
        'db_to_json_columns' : {
            'id_classe' : '_id',
            'nom_classe' : 'name',
            'desc_classe' : 'description'
        }        
    },
       
    TABLE_FLORA_INCLINES: {
        'id_col': 'id_pente',
        'json_name': 'v_modile_pentes',
        'sqlite_name': 'inclines',
        'select_col': 'id_pente, val_pente, nom_pente',
        'db_to_json_columns' : {
            'id_pente' : '_id',
            'val_pente' : 'value',
            'nom_pente' : 'name'
        }        
    },

    TABLE_FLORA_DISTURBANCES: {
        'id_col': 'id',
        'json_name': 'v_mobile_perturbations',
        'sqlite_name': 'disturbances',
        'select_col': 'codeper as id, codeper, classification, description',
        'db_to_json_columns' : {
            'id' : '_id',
            'codeper' : 'code',
            'classification' : 'classification',
            'description' : 'description'
        }        
    },

    TABLE_FLORA_PHENOLOGY: {
        'id_col': 'id',
        'json_name': 'v_mobile_phenologies',
        'sqlite_name': 'phenology',
        'select_col': 'codepheno as id, codepheno, pheno',
        'db_to_json_columns' : {
            'id' : '_id',
            'codepheno' : 'code',
            'pheno' : 'name'
        }        
    },

    TABLE_FLORA_PHYSIOGNOMY: {
        'id_col': 'id_physionomie',
        'json_name': 'v_mobile_physionomies',
        'sqlite_name': 'physiognomy',
        'select_col': 'id_physionomie, groupe_physionomie, nom_physionomie',
        'db_to_json_columns' : {
            'id_physionomie' : '_id',
            'groupe_physionomie' : 'group_name',
            'nom_physionomie' : 'name'
        }        
    },
    
    TABLE_FLORA_VISU_FP: {
        'id_col': 'indexzp',
        'json_name': 'v_mobile_visu_zp',
        'sqlite_name': 'prospecting_areas',
        'select_col': 'indexzp, cd_nom, st_asgeojson(st_transform(the_geom_2154,4326)) as geometry',
        'db_to_json_columns' : {
            'indexzp' : '_id',
            'cd_nom' : 'taxon_id',
            'geometry' : 'geometry'
        }        
    },

    TABLE_FLORA_SEARCH: {
        'id_col': 'gid',
        'json_name': 'v_mobile_recherche',
        'sqlite_name': 'search',
        'select_col': 'gid, to_char(dateobs,\'YYYY/MM/dd\') as dateobs, taxon, observateurs, geom_4326, centroid_x, centroid_y',
        'db_to_json_columns' : {
            'gid' : '_id',
            'dateobs' : 'dateobs',
            'taxon' : 'taxon',
            'observateurs' : 'observer',
            'geom_4326' : 'geometry',
            'centroid_x' : 'longitude',
            'centroid_y' : 'latitude'
        }        
    },    
}

FAUNE_TABLE_INFOS_GEOJSON =  {
    TABLE_FAUNA_UNITY_GEOJSON: {
        'id_col': 'id_unite_geo',
        'json_name': 'unity_geojson',
        'select_col': 'id_unite_geo, ST_AsText(ST_SnapToGrid(st_transform(the_geom,4326),0.00001)) as geom',
        'db_to_json_columns' : {
            'id_unite_geo' : 'id',
            'code_insee' : 'insee',
            'commune' : 'city',
            'geom': 'geometry'
        }        
    }
}

INV_TABLE_INFOS_GEOJSON =  {
    TABLE_INV_UNITY_GEOJSON: {
        'id_col': 'id_unite_geo',
        'json_name': 'unity_geojson',
        'select_col': 'id_unite_geo, ST_AsText(ST_SnapToGrid(st_transform(the_geom,4326),0.00001)) as geom',
        'db_to_json_columns' : {
            'id_unite_geo' : 'id',
            'code_insee' : 'insee',
            'commune' : 'city',
            'geom': 'geometry'
        }        
    }
}

#FLORA_TABLE_INFOS_GEOJSON =  {
    #TABLE_FLORA_UNITY_GEOJSON: {
        #'id_col': 'id_unite_geo',
        #'json_name': 'unity_geojson',
        #'select_col': 'id_unite_geo, ST_AsText(ST_SnapToGrid(st_transform(the_geom,4326),0.00001)) as geom',
        #'db_to_json_columns' : {
            #'id_unite_geo' : 'id',
            #'code_insee' : 'insee',
            #'commune' : 'city',
            #'geom': 'geometry'
        #}        
    #}
#}




MOBILE_SQLITE_SAMPLE = os.path.join(PROJECT_ROOT_PATH, "data.db.sample")

MOBILE_SQLITE_CREATE_QUERY = (
    'CREATE TABLE IF NOT EXISTS observers (_id INTEGER, ident TEXT, lastname TEXT, firstname TEXT, filter INTEGER)',
    'CREATE TABLE IF NOT EXISTS taxa_unities (unity_id INTEGER, taxon_id INTEGER, date TEXT, color TEXT, nb_obs INTEGER)',
    'CREATE TABLE IF NOT EXISTS taxa (_id INTEGER, name TEXT, name_fr TEXT, class_id INTEGER, number INTEGER, patrimonial INTEGER, message TEXT, filter INTEGER)',
    'CREATE TABLE IF NOT EXISTS criterion (_id INTEGER, name TEXT, sort INTEGER, class_id INTEGER)',
    'CREATE TABLE IF NOT EXISTS environments (_id INTEGER, name TEXT)',
    'CREATE TABLE IF NOT EXISTS inclines (_id INTEGER NOT NULL , value DOUBLE NOT NULL , name TEXT NOT NULL )',
    'CREATE TABLE IF NOT EXISTS phenology (_id INTEGER NOT NULL , code INTEGER NOT NULL , name TEXT NOT NULL )',
    'CREATE TABLE IF NOT EXISTS physiognomy (_id INTEGER NOT NULL ,group_name TEXT NOT NULL ,name TEXT NOT NULL )',
    'CREATE TABLE IF NOT EXISTS disturbances (_id INTEGER NOT NULL , code INTEGER NOT NULL , classification TEXT NOT NULL , description TEXT DEFAULT (null) )',
    'CREATE TABLE IF NOT EXISTS prospecting_areas (_id INTEGER NOT NULL , taxon_id INTEGER, geometry TEXT NOT NULL )',
    'CREATE TABLE IF NOT EXISTS search (_id INTEGER NOT NULL, dateobs TEXT, taxon TEXT NOT NULL, observer TEXT, geometry TEXT NOT NULL, longitude DOUBLE NOT NULL, latitude DOUBLE NOT NULL)',
    'CREATE TABLE IF NOT EXISTS android_metadata (locale TEXT DEFAULT "en_US")'
)


MOBILE_SQLITE_EXTRA_SQL = (
    'INSERT INTO android_metadata VALUES ("en_US")',
)

from settings_local import *
