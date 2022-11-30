# ob-django
OpenBootcamp Django course

## Patrón de arquitectura de Django
Se llama Model Template View (MTV) y es una variante de Model View Controller (MVC).

### MVC
1. Un usuario realiza una petición a una URL
2. Acude al diccionario que asocia cada URL a un controlador
3. El controlador contiene la lógica y se comunica con el modelo
4. El modelo contiene los datos. Puede tratarse como una clase y crear objetos.
5. El modelo se conecta a la base de datos
6. La base de datos devuelve información al modelo
7. El modelo devuelve la información al controlador
8. El controlador pasa esa información a la vista
9. La vista muestra la información al usuario

```
USUARIO ---> URL ---> CONTROLADOR <--> MODELO <---> BASE DE DATOS
  ^                         |
  |                         |
  |                         V
  ----------------------- VISTA
```

### MTV
Es igual que el MVC con la diferencia de que a los controladores los llamammos vistas y a las vistas las llamamos plantillas.

```
USUARIO ---> URL ---> VISTA <--> MODELO <---> BASE DE DATOS
  ^                     |
  |                     |
  |                     V
  ----------------- PLANTILLA
```

## Estructura de archivos
Tenemos: 
* 1 directorio: [nombredelproyecto]
  * 
* 1 archivo: **manage.py**, que se encarga de manejar el proyecto

Cada aplicación es gestionada como un paquete (una carpeta). Cada una tiene su archivo __init__.py

Los archivos **asgi.py** y **wsgi.py** son auxiliares y nos ayudan a trabajar con servidores de prueba y otras acciones auxiliares.

El archivo **urls.py** asocia urls con las vistas correspndientes.

Por úlitmo, **settings.py** establece las configuraciones del paquete. Por ejemplo, incluye apps instaladas por defecto, utilidades de middleware, la configuración de la base de datos, entre otros.

## Hola mundo
Vamos a crear una vista que devuelva un "Hola mundo":

1. Crear la estructura de base de datos necesaria para poder funcionar. Cada vez que modifiquemos la estructura de datos:

```
python manage.py migrate
```

2. Lanzar el servidor

```
python manage.py runserver
```

3. Creamos el archivo de vistas views.py. Definimos la función con sus parámetros. Las vistas siempre van a tener, por lo menos, un parámetro, que es la petición.
4. Asociamos la vista con la url

```
path('saludo/', views.saludo, name='saludo')

```

## Rutas con parámetro
Vamos a crear urls dinámicas incluyendo parámetros en ellas.
1. Escribir la url con el parámetro entre <> y marcando el tipo de dato

```
path('post/<int:id>/')
```