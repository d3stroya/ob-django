from django.forms import ModelForm
from .models import Employee
    
class EmployeeForm(ModelForm):
    class Meta:
        # El modelo que queremos asociar
        model = Employee

        # Campos del modelo que queremos incluir
        #fields = ['first_name', 'email']

        # Atajo para para incluir todos los campos
        fields = '__all__'

        # Podemos indicar que quiero todos menos alguno concreto
        #exclude = ('email')
        exclude = ['last_name', 'email']