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

# Comunicar aplicaciones con el proyecto
1. Creamos un archivo urls.py en la aplicación y añadimos las urls
2. Definimos las vistas en views.py
3. Ahora conectamos aplicación y proyecto:
   1. En urls.py del poryecto, añadimos una ruta que incluya el archivo urls.py de la aplicación:
   ```
   path('comentarios/', include('comentarios.urls'))
   ```
   2. Ahora podemos acceder a la aplicación desde la ruta (en este caso) /comentarios y a la vista de prueba desde la ruta /comentarios/test

# Crear y borrar objetos
Para crear:
1. Creamos una ruta
2. Importamos el modelo en views.py
3. Creamos un objeto
4. Guardamos el comentario en base de datos
   ```
    comment = Comment(1, "Franky", 10, "Comentario de prueba")
    comment.save()
   ```
5. También podemos hacerlo en una sola línea
   ```
   comment = Comment.objects.create(name="Bridget")
   ```

Para borrar:
1. Creamos una ruta
2. Creamos la vista
3. Buscamos el objeto que queremos borrar
   ```
   comment = Comment.objects.get(id=1)
   ```
4. Borramos el objeto
´´´
comment.delete()
```
5. También podemos borrar el objeto filtrando por alguno de sus atributos:
```
Comment.objects.filter(id=2).delete
```