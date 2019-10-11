collectstatic:
	cd alignmentpro && python manage.py collectstatic

gunicornserver:
	cd alignmentpro && gunicorn -b 0.0.0.0:8080 --workers=9 --threads=2 alignmentpro.wsgi
