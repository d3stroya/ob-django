# OpenCode Diciembre - Wishlist
Vamos a crear un CRUD con Django que permita añadir productos a una lista de deseos.

Cada producto tendrá un título, una descripción, un precio, una imagen y un enlace.

## Configuraciones iniciales
1. Creo la aplicación 'product'.
2. En settings.py: 
   1. instalo dicha aplicación
   2. añado el directorio 'templates' y lo creo en el proyecto
   3. añado las rutas de estáticos y creo la aplicación 'static' en el proyecto
   4. creo la base de datos postgresql y la añado a settings.py
3. Compruebo que la aplicación está instalada
4. Hago las migraciones a la base de datos
5. Añado a urls.py las urls de la aplicación

## Creación del modelo
1. Creo el modelo Product
2. Añado un archivo forms.py para crear un formulario a partir del modelo
3. Defino las rutas y las vistas
4. Diseño el frontend en la carpeta templates
