py manage.py makemigrations --dry-run --verbosity 3
py manage.py runserver
py manage.py createsuperuser
pip install coverage
coverage run --omit='_/venv/_' manage.py test
coverage html
pip install djangorestframework