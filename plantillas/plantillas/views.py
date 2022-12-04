from django.shortcuts import render


def simple(request):
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categories = ['action', 'drama', 'thriller']

    # Defino el contexto
    context = { 'name': name, 'categories': categories }

    return render(request, 'dinamico.html', context)

def simple(request, color):
    context = { 'color': color }
    return render(request, 'simple.html', context)
