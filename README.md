= Liberador =

WIP

Toma un ZIP de CSVs y lo mapea a los modelos de cada app para insertarlo en la base de datos y proveer una api.

Se puede adaptar a múltples fuentes de datos mediante creación de múltiples apps, cada app tiene que definir sus modelos para lograr la importación y sus viewsets para tener API.

== TODO ==
* Modelos relacionados
* Exportar algunos CSVs cada vez que se importa
* Definir endpoints de la API para filtros y búsquedas
* Manejo de usuarios asociados a cada app
* Except fields from model to CsvDbModel

==Instalacion==

* clone
* mkvirtualenv csoapi
* pip install -r requirements.txt
* ./manage.py migrate
* ./manage.py runserver
