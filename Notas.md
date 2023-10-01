
# Instalaciones

## Crear entorno virtual para el proyecto
```python -m venv venv```


## Install Django 4.2.4
```pip install django==4.2.4```


## Crear proyecto en Django en la carpeta raiz
```django-admin startproject <nombre_proyecto> . ```


## Crear nuevo app
```python manage.py startapp <app_name>```


## Add Django Rest Framework
https://pypi.org/project/djangorestframework/
```pip install djangorestframework``` 


## Add drf-yasg
https://pypi.org/project/drf-yasg/
```pip install drf-yasg``` 


## Renderizar archivos estaticos
```python manage.py collectstatic```


## Cambiar el modelo User
* 1. Eliminar las migraciones del proyecto
* 2. Eliminar base de datos 
* 3. Crear el modelo User por defecto
* 4. Volver a correr las migraciones


## Crear usuario
```python manage.py createsuperuser```


## Add decouple - Para la separación estricta de la configuración de código
https://pypi.org/project/python-decouple/ 
```pip install python-decouple```


## Add psycogp2 para conectar base de datos Postgres
https://pypi.org/project/psycopg2/ 
```pip install psycopg2```


## djangorestframework-simplejwt 
https://pypi.org/project/djangorestframework-simplejwt/
```pip install djangorestframework-simplejwt```
```pip install djangorestframework-simplejwt[crypto]```


## Add Dumpdata
```python manage.py dumpdata > api_blog.json```


## Load Dumpdata
```python manage.py loaddata api_blog.json```