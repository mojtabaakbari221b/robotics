python ./manage.py collectstatic --no-input
python ./manage.py migrate
DJANGO_SETTINGS_MODULE=gunicorn robotic.wsgi:application --bind 0.0.0.0:8000 --workers 3
