# aee-oscar
aee outlet store built on [django-oscar](https://github.com/django-oscar/django-oscar)

## Installation

```
pew new AEE_OSCAR
pip install \
  django django-oscar django-compressor django-widget-tweaks django-registration \
  pycountry
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

## Dev notes
```
django-admin startproject project .
./manage.py migrate
./manage.py runserver
django-admin startapp app
# add 'app' to project/settings.py INSTALLED_APPS
# follow instructions at http://docs.oscarcommerce.com/en/latest/internals/getting_started.html
```
