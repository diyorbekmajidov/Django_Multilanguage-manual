# Django_Multilanguage-manual
# Hello dear, how can I translate the django admin panel?

### First of all, I create a 

```bash
mkdir DjangoMultilanguage
cd DjangoMultilanguage
mkdir templates
mkdir static

django-admin startproject myproject .
python manage.py startapp mysite


```
### So Than I creat virtual environment
```
1. python3 -m venv venv
than venv activate
2. source venv/bin/activate
```

### In the project setting.py file, add app:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite',  #your created app name
]
```
### Configure templates in the project setting.py file:
```
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'International.context_processors.logo_context',
                'django.template.context_processors.i18n',
            ],
        },
    },
]
```
