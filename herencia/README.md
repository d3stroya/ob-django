# Herencia de plantillas
Evitan duplicar código.

1. Definimos una plantilla base que contendrá todo el contenido común e indicará bloques de contenidos que rellenarán otras plantillas.
```
{% block nombrebloque %}{% endblock nombrebloque %}
```

2. En otra plantilla, indicamos el bloque que vamos a rellenar y añadimos el contenido.
```
{% block content %}
    <h2>Herencia</h2>
    Content:
    {% lorem 3 p random %}
{% endblock content %}
```

## Enlaces
Usaremos enlaces referenciados por su nombre en django en lugar de por la url, de manera que podamos cambiar las url en url.py sin tener que modificar el código html.
Para ello:
```
<li><a href="{% url 'otra' %}">Otra</a></li>
```

## Incluir partes de código de una plantilla en otra
En este caso no queremos heredar, sino dividir el código en varios documentos. 

Sacamos el menú de base.html y lo pasamos a otro archivo (menu.html) dentro de una nueva carpeta partials, que está dentro de layouts.

Para pintarlo en el dom, usamos la etiqueta include:
```
{% include './partials/menu.html' %}
```