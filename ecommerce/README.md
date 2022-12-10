# Panel de administración
* Accedemos a él desde /admin
* Para acceder, necesitamos crear un usuario:
```
python manage.py createsuperuser
```
* Vamos a poder gestionar grupos y usuarios.
  * Crearemos usuarios
  * Crearemos grupos
    * Daremos permisos concretos a grupos concretos

## Registrar modelos en el panel de administración
En admin.py, importamos el modelo que queramos y escribimos:
````
admin.site.register([Modelo])
```

Podemos mejorar la gestión en el panel de administración:
* Importar ModelAdmin
* Creamos una clase con el nombre del modelo:
```
class ProductAdmin(ModelAdmin):
    list_display = ("name", "short_description", "stock")
```
* Añadimos ProductAdmin a admin.site.register
* Añadimos una barra de búsqueda
```
search_fields = ("name", "short_description")
````
* Añadimos filtros
```
list_filter = ("name", "stock")
```
* Podemos añadir jerarquías de datos con date_hierarchy
* Podemos cambiar el lenguaje desde settings.py