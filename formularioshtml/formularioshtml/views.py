from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request, 'form.html', {})

def getgoal(request):
    # Gestionamos el método de envío
    if request.method != 'GET':
        return HttpResponse('Error')
    
    # Accedemos a los datos enviados en el formulario y lo añadimos al contexto
    name = request.GET['name']
    email = request.GET['email']
    return render(request, 'success.html', {'name': name, 'email': email})

def postform(request):
    

    return render(request, 'postform.html', {})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse('Método GET no soportado')

    deseo = request.POST['deseo']    
    return render(request, 'postsuccess.html', {'deseo': deseo})
    