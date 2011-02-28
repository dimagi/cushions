DATABASES = {
    'default': {
        'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cushions.sqlite',              # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

####### Couch Forms ######
# Add custom couch settings here
#COUCH_SERVER_ROOT = 'localhost:5984'
#COUCH_DATABASE_NAME = 'cushions'
#COUCH_USERNAME = 'admin'
#COUCH_PASSWORD = 'password'

DEBUG=True
TEMPLATE_DEBUG=DEBUG