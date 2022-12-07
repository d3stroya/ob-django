# Formularios a partir de modelos
1. En forms.py
   1. Importamos ModelForm de django.forms
   2. Importamos el modelo
   3. Creamos una clase EmployeeForm(ModelForm)
   4. Añadimos una clase Meta
      1. Indicamos el modelo que queremos vincular (como clase)
      2. Indicamos los campos del modelo que queremos incluir (como array)
2. En views.py:
   1. Creamos un objeto formulario
   2. Lo pasamos por contexto
3. Pintamos el formulario en el html