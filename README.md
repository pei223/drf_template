# drf_sample
Sample REST API Web application with django/djangorestframework.


## Functions
- Authentication
    - Using django-rest-auth
- Blog and Comments

<br><br>

## Setup
### Production
Set .env file to root directory.
Please refer to sample.env file.
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Local
```
pip install -r requirements.txt
python manage.py makemigrations --settings=config.local_settings
python manage.py migrate --settings=config.local_settings
```

<br><br>


## Deploy
### Local
```
python manage.py runserver --settings=config.local_settings
```

### Production
```
python manage.py collectstatic
gunicorn --env DJANGO_SETTINGSMODULE=config.settings config.wsgi:application --bind <IP Address>:<Port> -w 5 --threads 5 -D --log-syslog --access-logfile access.log --log-file error.log
```

<br><br>

## Test
```
python manage.py makemigrations --settings=config.test_settings
python manage.py migrate --settings=config.test_settings
python manage.py runserver --settings=config.test_settings

coverage run --source='./app' manage.py test app --settings=config.test_settings
coverage report
coverage html
```

## References
- https://www.django-rest-framework.org/
- https://django-rest-auth.readthedocs.io/en/latest/installation.html
