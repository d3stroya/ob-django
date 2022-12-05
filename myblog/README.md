# Modelado de datos interrelacionados (claves foráneas)
Para relacionar unos modelos con otros simplemente debemos crear un atributo referenciando al otro modelo:
```
author = models.ForeignKey(Author)
```

Necesitamos definir qué hacer cuando se borre un registro con clave foránea:
```
author = models.ForeignKey(Author, on_delete=models.CASCADE)
```
 También podemos definirlo para la actualización de datos

 # Crear datos faltos para añadir a la BD
 https://github.com/Brobin/django-seed

 # Consulta de datos
 1. Creamos un archivo queries.html dentro de myblog > templates > post
 2. En views.py importamos los modelos
 3. Definimos la vista que renderice queries.html
    1. Creamos las peticiones
    2. Incluimos los objetos en el contexto:
 4. Pintamos los datos en el html

Más info: https://docs.djangoproject.com/en/4.1/topics/db/queries/