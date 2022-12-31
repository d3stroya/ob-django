# Clone de Twitter con Django
Tutorial: https://www.youtube.com/watch?v=06aDhOwqvfY

## Configuraciones iniciales
1. Crear entorno virtual con ```python3 -m venv socialenv``` y entrar en él.
2. Empezar projecto con ```django-admin startproject twitterClone```. Entrar en él.
3. Crear app twitter con ``` python3 manage.py startapp twitter```.
4. Instalar la app en settings.py añadiéndota a la lista de INSTALLED_APPS. Comprobamos que se ha instalado con ```check```.
5. Copiamos la carpeta static del proyecto de referencia y lo pegamos en nuestra app.
6. Añadimos a urls.py las urls de la app twitter.
7. Creamos la base de datos y la conectamos al proyecto en settings.py > DATABASES
8. Crear un superusuario con ```python3 manage.py createsuperuser```

## Modelos
1. En models.py, importamos User y timezone.
2. Creamos una clase Profile para extender la clase User, añadiéndole una bio y una imagen.
3. Creamos una clase Post que ordene los tuits según la fecha de más recientes a más antiguos.
4. Hacemos las migraciones

## Vistas
1. Diseñamos las plantillas html
2. Creamos las vistas y sus rutas
3. Importamos la librería humanize para mostrar la hora de una formal más amigable: https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/
4. Vamos añadiendo los datos dinámicos.
   1. Para acceder a los datos del usuario actual: ```request.user.<propiedad>```. Request es lo que aporta la info de quién es el usuario actual.

## Registro
1. Creamos un forms.py
2. Definimos la clase UserRegisterForm con una clase meta que asocie el formulario al model y escogemos los campos que queremos mostrar.
3. Creamos la vista
4. Creamos una carpeta forms y dentro un archivo register.html
5. Añadimos la url
6. Diseñamos el html
7. Añadimos la funcionalidad a la vista
8. Agregamos los inputs del formulario al html

## Login
1. En urls importamos LoginView y LogoutView y añadimos las urls de login/ y logout/
2. En settings.py añadimos 
```LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
```
3. Editar la plantilla login.html
4. Añadir un condicional que muestre un mensaje si hay errores en el formulario, como usuario o contraseña incorrecta.

## Tuits
1. En forms.py definimos PostForm
2. Añadir la lógica del formulario en views > home
3. En el html cambiamos el input por el campo del formulario
4. Añadimos el method POST al form
5. Agregamos también el csrf_token

## Eliminar post
1. Definimos la vista
2. Creamos la ruta delete/ con el parámetro post_id
3. Añadimos la ruta al botón del html
4. Creamos un condicicional para que solo se muestre este icono en los tuits propios y no podamos borrar los tuits de otras personas.

## Imágenes
1. En settings.py añadir 
```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
2. En urls.py añadir 
```
from django.conf import settings
from django.conf.urls.static import static
```
3. Añadir también ```+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)```
4. Definir la propiedad imagen en el modelo
5. Subir imágenes de perfil desde /admin
6. Mostrarlas en el html

## Perfil
1. Crear la vista
2. Definir la url con el parámetro dinámico <str:username>/
3. Crear el html

## Editar el perfil
1. Definir vista
2. Crear la url
3. Añadir botón para editar perfil en la página profile
4. Crear un formulario UserUpdateForm
5. Importamos los formularios en views.py y definimos la lógica de edit()
6. Diseñamos el html

## Seguir y dejar de seguir
1. Crear modelo Relationships para persistir las relaciones entre usuarios
2. Añadir una funcionalidad (following) al modelo Profile
3. Añadir otra para followers
4. Hacer las migraciones
5. Agregar las relacoines a admin
6. Crear la vista para follow y para unfollow
7. Añadimos las urls
8. Implementamos unfollow
9. TODO: cuenta de seguidores y seguidos

## Proteger rutas
1. En views.py import decorador login_required
2. Añadir @login_required a las vistas que queramos proteger
3. Agregar en settings.py ```LOGIN_URL = 'login'```
