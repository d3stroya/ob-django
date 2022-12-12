from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse

def list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/list.html', context)

def save_product(request):
    if(request.method == 'POST'):
        product = ProductForm(request.POST)
        if product.is_valid:
            product.save()
            
            products = Product.objects.all()
            context = {'products': products, 'product': products}
            return render(request, 'product/list.html', context)

    else:
        return render(request, 'layout/create.html', {'product': product})

def create(request):
    form = ProductForm()
    context = {'form': form}
    return render(request, 'product/create.html', context)

def delete(request, id):
    if(request.method == 'GET'):
        product = Product.objects.get(id=id)
        product.delete()
        
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'product/list.html', context)

def update(request, id):
    product = Product.objects.get(id=id)
    if(request.method == 'GET'):
        form = ProductForm(instance=product)
        context = {'form': form, 'id': id}
        return render(request, 'product/update.html', context)

    if(request.method == 'POST'):
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            
            products = Product.objects.all()
            context = {'products': products}
            return render(request, 'product/list.html', context)