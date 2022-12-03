# Archivos estáticos

En settings.py, tenemos un STATIC_URL con la ruta '/static'.

1. Creamos la carpeta static, donde almacenaremos todos los archivos estáticos del proyecto (css, js, imágenes).
2. Creamos un style.css en /static
3. Agregamos la etiqueta {% load static %} en el html
4. También en el html, agregamos el estático en en el link ref: href="{% static 'style.css' %}">
5. En settings.py añadimos la variable de entorno STATICFILES_DIRS:
STATICFILES_DIRS = [
    BASE_DIR / "static", --> define la carpeta static como directorio base. Hace que el doc busque los arcivos estáticos desde ella, que es donde van a estar todos los archivos estáticos.
    '/var/www/static' --> para producción
]