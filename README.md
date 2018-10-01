# aee-oscar
aee outlet store built on [django-oscar](https://github.com/django-oscar/django-oscar)


## Installation

```
pew new -r requirements.txt AEE_OSCAR
# copy project/settings.py.dist to project/settings.py and modify as needed
./manage.py migrate
./manage.py oscar_populate_countries --initial-only
# manually delete "blacklisted" countries in Lebanon
./manage.py runserver
```

For a reference on django-registration
- https://devdoodles.wordpress.com/2009/02/16/user-authentication-with-django-registration/


## Usage

- browse at http://localhost:8000
- can also go to /dashboard
- or to /admin


## Changelog
Check [[CHANGELOG.md]]


## Dev notes
```
django-admin startproject project .
./manage.py migrate
./manage.py runserver
django-admin startapp app
# add 'app' to project/settings.py INSTALLED_APPS
# follow instructions at http://docs.oscarcommerce.com/en/latest/internals/getting_started.html

# to create postgresql database for django
# https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
sudo su - postgres
psql
create database aee_oscar;
...
```
