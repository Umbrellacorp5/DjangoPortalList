# DjangoPortalList

conexion postgres

Instalar librerias necesarias
pip install -r ./PortalList/requirements.txt
pip3 freeze > requirements.txt / si se instala otra libreria

chmod a+x build.sh /ace ejecutable build.sh

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

SQLite
para manejar SQLlite desde VScode descarguen la extension SQLite 
control + T para que les aparezca la barra
borran lo que haya y escriban >SQL
le dan a OPEN SQL... y seleccionan mydatabase.db
se les abrira abajo a la izquierda, debajo de los archivos
Para hacer una Query pueden escribir en el archivo --SQLite.sql o click derecho en la DB nueva query

API
python manage.py shell


https://pythonhosted.org/djeneralize/defining_models.html

indian project: https://github.com/neyamul-sbr/university_management_system_extend