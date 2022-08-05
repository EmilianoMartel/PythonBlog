from django.shortcuts import render
from products.models import Film

# Create your views here.
def list_products(request):
    Films = Film.objects.all()
    context = {
        'Film':Films
    }
    return render(request, 'products/product_list_cards.html', context=context)