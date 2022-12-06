from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request, 'form.html', {})

def goal(request):
    # Gestionamos el método de envío
    if request.method != 'GET':
        return HttpResponse('Error')
    
    # Accedemos a los datos enviados en el formulario y lo añadimos al contexto
    name = request.GET['name']
    email = request.GET['email']
    return render(request, 'success.html', {'name': name, 'email': email})
    