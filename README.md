# Liberador

WIP

Aplicación para liberar datos. Genera CSVs y una API a partir de una fuente de datos.

En esta versión toma un ZIP que contiene archivos CSV exportados de otro sistema y lo mapea a model internos (soporta múltiples apps con sus modelos), lo guarda en una base de datos, exporta CSVs y una API.

Se puede adaptar a múltples fuentes de datos mediante creación de múltiples "apps", cada app tiene que definir sus modelos para lograr la importación y sus viewsets para tener API. Cada app puede definir qué tablas se exportan automáticamente a CSV y endpoints personalizados en la API.

## Instalacion

* clone
* mkvirtualenv libera
* pip install -r requirements.txt
* ./manage.py migrate
* ./manage.py runserver

## Crear una app
Estando parado en el directorio donde descargamos el repositorio y con el virtualenv activado, ejecutar:
* django-admin startapp [nombre]

Luego editar models.py y crear los modelos para cada campo, cada modelo debe indicar el nombre del archivo que mapea. También se deben crear ViewSets para cada modelo en views.py.

## TODO
* Modelos relacionados
* Definir endpoints de la API para filtros y búsquedas
* Manejo de usuarios (limitar quién puede cargar datos a cada app)
