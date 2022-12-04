# Modularización
Para optimizar el código y cada proyecto, crearemos aplicaciones individuales que juntas conformen el proyecto. 
Es decir, dividir el problema general en subproblemas más pequeños y resolverlos con aplicaciones.

Para ello:
```
python manage.py startapp [nombreaplicacion]
```

Podemos usar una aplicación en otro proyecto simplemente copiando la carpeta de la aplicación.

En settings.py > INSTALLED_APPS añadimos el nombre de la aplicaicón.


Además, podemos comprobar que una aplicación está instalada en el proyecto:
```
python manage.py check [nombreaplicacion]
```

# Modelos de datos
En Django trabajaremos con clases y por detrás el ORM va a crear tablas. 
Los atributos de las clases serán las columnas de las tablas.

De esta manera, el proyecto será independiente del servicio de BD (PostgreSQL, MySQL,...).

Crearemos las estructuras de datos (los modelos) en models.py.

Después, tenemos que pedirle a Django que pase los datos a SQL:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Cada vez que hagamos cambios, tendremos que repetir estas dos indicaciones.

Toda la info de las migraciones se van guardando en db.sqlite3 > django.migrations y en [nombreaplicacion]/migrations