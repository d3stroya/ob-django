from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

def form(request):
    # Podemos pasar unos valores por defecto al formulario
    commentForm = CommentForm({'name': 'Franky', 'url': 'https://idonteatsausag.es', 'comment': 'no f*cking way'})
    return render(request, 'form.html', {'commentForm': commentForm})

def goal(request):
    if request.method != 'POST':
        return HttpResponse('Método GET no soportado')

    return HttpResponse('Hola, ' + request.POST['name'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        # Comprobamos si los datos son válidos
        if form.is_valid():
            return HttpResponse('POST')
        else: 
            return render(request, 'widget.html', {'form': form})