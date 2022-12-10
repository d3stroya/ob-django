from django.shortcuts import render
from .forms import ProductForm, Product

def index(request):
    return render(request, 'index.html', {})

def add(request):
    # Acciones si recibimos datos
    if request.method == 'POST':
        # Creamos un objeto del formulario con los datos introducidos
        form = ProductForm(request.POST)
        # Validamos los datos
        if form.is_valid():
            # Guardamos los datos
            form.save()
            # Devolvemos una vista
            return render(request, 'index.html', {})
    else:
        form = ProductForm()
        return render(request, 'add-product.html', {'form': form})

def update(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
    else:
        form = ProductForm()
        return render(request, 'update-product.html', {'form': form}) 

def allProducts(request):
    allProducts = Product.objects.all()
    return render(request, 'all-products.html', {'allProducts': allProducts})
