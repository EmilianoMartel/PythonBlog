from django.shortcuts import render
from products.models import Producto

# Create your views here.
def list_products(request):
    products = Producto.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products/product_list_cards.html', context=context)