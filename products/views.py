from django.shortcuts import render
from products.models import Producto, Contenido

# Create your views here.
def list_products(request):
    products = Producto.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products/product_list_cards.html', context=context)
    
def list_content(request):
    content = Contenido.objects.all()
    context = {
        'contents':content
    }
    return render(request, 'products/content_list_cards.html', context=context)