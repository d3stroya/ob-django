# Plantillas
1. Creamos un nuevo proyecto: ```django-admin startproject [nameproject]```
2. Migramos la estructura: ```python manage.py migrate```
3. Levantamos el servidor: ```python manage.py runserver```
4. Vamos a urls.py y creamos una nueva ruta
5. Creamos el archivo views.py
   1. Ahora vamos a devolver plantillas (HTML) en lugar de respuestas HTTP. Las plantillas permiten separar la lógica de lo visual, así como evitan repetir código.
6. Accedemos a settings.py > TEMPLATES > DIRS y añadimos 'templates'.
7. Creamos el directorio templates en el directorio raíz del proyecto (debe coincidir con la ruta que hemos indicado en settings.py).
8. Dentro de templates, creamos simple.html.
9. Volvemos a views.py para devolver la plantilla:
   1.  Importamos render 
   2.  Devolvemos el método render con los parámetros:
       1.  request
       2.  plantilla
       3.  contexto

## Uso de contextos
1. Creamos una nueva ruta (dinamico)
2. Definimos la vista en views.py y con el contexto
3. Creamos la plantilla y pasamos el contexto donde queremos la info dinámica. 
4. Vamos a añadir un array para mostrarlo
5. Pasamos el array en el html


## Bucles y condicionales
Para recorrer el array del epígrafe anterior:
* Usamos {% %}
* Y cerramos el bucle con endfor
* Entre medias, las acciones
```
{% for category in categories %}
    <li>{{category}}</li>
{% endfor %}    
```

## Filtros y comentarios
Podemos pintar comentarios que no se pintarán en el html:
* Comentario simple: {# #}
* Comentario multilínea: {% comment %} {% endcomment %}

También podemos aplicar filtros: |[filtro]
Por ejemplo:
```
{{ category|upper }}
{{ categories|length }}
```
