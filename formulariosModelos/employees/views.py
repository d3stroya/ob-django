from django.shortcuts import render
from .forms import EmployeeForm

def index(request):
    # Creamos un objeto de clase EmployeeForm (un formulario)
    form = EmployeeForm()
    # Pasamos el formualrio por contexto
    return render(request, 'index.html', {'form': form})