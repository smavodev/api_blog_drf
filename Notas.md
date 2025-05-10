
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


## Add Filtros 
https://pypi.org/project/django-filter/
```pip install django-filter```


## Add Pillow 
https://pypi.org/project/Pillow/
```pip install pillow```

## Subir las migraciones a la base de datos
```python manage.py makemigrations```
```python manage.py showmigrations```
```python manage.py migrate```

## Add Dumpdata
```python manage.py dumpdata > api_blog.json```

## Load Dumpdata
```python manage.py loaddata api_blog.json```


### Backup de librerias instaladas
```pip freeze > requirements.txt```

### Instalar librerias desde requirements.txt
```pip install -r requirements.txt```


### Importante:
Una vez clonado el repositorio asegurate de primero crear la base de datos antes de levantar el proyecto.
- Instalar dependencias
- Registrar BD (Postgresql)
- Correr las migraciones
- Levantar el proyecto en local


### Acceso Admin
http://127.0.0.1:8000/admin/
Usuario: smavodev@gmail.com
Password: 1nd1.sm4rT%%

### Swagger API Docs
http://127.0.0.1:8000/docs/

### Api Docs
http://127.0.0.1:8000/redocs

### URL API
http://127.0.0.1:8000/api/
http://127.0.0.1:8000/api/categories/
http://127.0.0.1:8000/api/posts/
http://127.0.0.1:8000/api/comments/