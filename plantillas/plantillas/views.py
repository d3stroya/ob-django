from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categories = ['action', 'drama', 'thriller']

    # Defino el contexto
    context = { 'name': name, 'categories': categories }

    return render(request, 'dinamico.html', context)

def categories(request):
    pass
