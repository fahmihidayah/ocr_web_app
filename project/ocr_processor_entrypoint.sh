sleep 10
#python manage.py rundramatiq
python -m celery -A project --workdir project worker -l INFO
