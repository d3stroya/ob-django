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