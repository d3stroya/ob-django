# Formularios Django
1. Creamos un archivo forms.py, donde definiremos las clases de cada formulario
   1. Importamos los formularios desde django
   2. Creamos la clase de manera similar a los modelos.
2. En views.py: 
   1. Importamos el formulario
   2. Creamos un objeto formulario dentro de la vista form
   3. Pasamos el objeto por contexto
3. Pintamos el formulario en forms.html
4. Podemos incluir algunos valores como "as_p" para que los campos del formulario se pinten como una etiqueta p.

## Dar estilos al formulario
1. Creamos una clase con sus atributos
2. Creamos una ruta
3. Y definimos una vista con un objeto de clase ContactForm y lo pasamos por contexto
4. En forms.py usamos widgets para indicar el tipo de etiqueta que será en html y el atributo que queremos darle, por ejemplo, clase y su nombre. 
5. Aplicamos estilos propios o externos como Bootstrap

# Validación de datos
Usamos el condicional con request.is_valid para definir qué acciones ejecutar cuando los datos son válidos y qué hacer cuando no lo son.

## Funciones clean
Podemos añadir validaciones extra a los campos del formulario con: def clean_[nombrecampo](self)

En views.py vamos a devolver la plantilla del formulario en caso de que haya error y esto mostrará el mensaje de error que hemos definimo de forms.py > clean_name

