# DjangoPortalList

conexion postgres

pip install dj-database-url psycopg2-binary
pip install whitenoise[brotli]
?python manage.py collectstatic
pip install gunicorn

chmod a+x build.sh

pip3 freeze > requirements.txt


Documentation

Part 1: Requests and responses https://docs.djangoproject.com/en/4.1/intro/tutorial01/
Part 2: Models and the admin site https://docs.djangoproject.com/en/4.1/intro/tutorial02/
Part 3: Views and templates https://docs.djangoproject.com/en/4.1/intro/tutorial03/
Part 4: Forms and generic views https://docs.djangoproject.com/en/4.1/intro/tutorial04/
Part 5: Testing https://docs.djangoproject.com/en/4.1/intro/tutorial05/
Part 6: Static files https://docs.djangoproject.com/en/4.1/intro/tutorial06/
Part 7: Customizing the admin site https://docs.djangoproject.com/en/4.1/intro/tutorial07/

Video de referencia a seguir
General: https://www.youtube.com/watch?v=T1intZyhXDU
Login y Deploy: https://www.youtube.com/watch?v=e6PkGDH4wWA


SQL
python manage.py makemigrations app
python manage.py sqlmigrate app 0001
python manage.py check /chequea por problemas
python manage.py migrate /migra

API
python manage.py shell

