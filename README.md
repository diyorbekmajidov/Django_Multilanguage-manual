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
        'DIRS': [os.path.join(BASE_DIR,'templates/')],# change direction
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'International.context_processors.logo_context',
                'django.template.context_processors.i18n', # add that code
            ],
        },
    },
]
```
### Setting static in the project setting.py file:
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
```
### Setting the language in the project setting.py file:
```
LANGUAGES = (
    ('ru',  'Russian'),
    ('en',  'English'),
    ('uz',  'Uzbek')
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
```
### Change Middleware Enter:
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',              # add
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

### Create an admin folder in the teplate folder
#### And create a base_site.html file inside it and put this code
```
{% extends "admin/base.html" %}
{% load i18n %}

{% block extrahead %}
{{ block.super }}
<style>
    /* Add custom styles here, if needed */
    .language-form {
      display: inline-block;
    }
    .language-label {
      display: inline-block;
      margin-right: 5px;
    }
    .language-select {
      display: inline-block;
    }
  </style>
{% endblock %}

{% block userlinks %}
  {{ block.super }}

  <form class="language-form" id="languageForm" method="post" action="{% url 'set_language' %}">
    {% csrf_token %}
    <label class="language-label" for="language">Lang:</label>
    <select class="language-select" name="language" id="language" onchange="changeLanguage(this.value)">
        {% for lang_code, lang_name in LANGUAGES %}
            {% if lang_code == LANGUAGE_CODE %}
                <option value="{{ lang_code }}" selected>{{ lang_name }}</option>
            {% else %}
                <option value="{{ lang_code }}">{{ lang_name }}</option>
            {% endif %}
        {% endfor %}
    </select>
  </form>

  <script>
    function changeLanguage(languageCode) {
      const form = document.getElementById('languageForm');
      form.elements.language.value = languageCode;
      form.submit();
    }
  </script>

{% endblock %}
```