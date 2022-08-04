from django.shortcuts import render

# Create your views here.
def list_products(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request, 'products/product_list_cards.html', context=context)