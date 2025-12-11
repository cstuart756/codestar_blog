# DEBUG should be False for deployment
DEBUG = False

# Add your Heroku app hostname
ALLOWED_HOSTS = ['your-app-name.herokuapp.com']

# Ensure blog app is installed
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
