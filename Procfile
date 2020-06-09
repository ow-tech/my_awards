release: python3 manage.py makemigrations
release: python3 manage.py migrate

web: gunicorn myawards.wsgi --log-file -

