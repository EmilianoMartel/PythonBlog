from django.shortcuts import render
from products.models import Producto, Contenido, Reseña

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

def list_review(request):
    review = Reseña.objects.all()
    context = {
        "reviews":review
    }
    return render(request, "products/review_list_card.html", context=context)