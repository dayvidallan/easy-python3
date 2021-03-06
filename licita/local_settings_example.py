DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'licita',
        'USER': 'postgres',
        'PASSWORD': 'licitaeasy',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}



EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'senha' #my gmail password
EMAIL_HOST_USER = 'email@gmail.com' #my gmail username
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


#dados do zoho, nosso servidor de email
#SMTP Host: smtp.zoho.com
#SMTP Port: 465

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    ADMINS = (
        ('Walkyso', 'walkyso@gmail.com'),
    )

SITE_URL = DEBUG and 'http://localhost:8000' or 'http://guamareserver.easygestaopublica.com.br:86'
