from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-product/', views.add, name='add'),
    path('update-product/', views.update, name='update'),
    path('all-products/', views.allProducts, name='products')
]
