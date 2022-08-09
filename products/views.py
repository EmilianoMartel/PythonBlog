from django.shortcuts import render, redirect
from products.models import Producto, Contenido, Reseña
from products.forms import Forms_contenido, Forms_review

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
    reviews = Reseña.objects.all()
    context = {
        "reviews":reviews
    }
    return render(request, "products/review_list_card.html", context=context)

def new_content(request):
    if request.method == "POST":
        form = Forms_contenido(request.POST)
        if form.is_valid():
            Contenido.objects.create(
                name = form.cleaned_data["name"],
                score = form.cleaned_data["score"],
                category = form.cleaned_data["category"],
                image_url = form.cleaned_data["image_url"],
                description = form.cleaned_data["description"],
            )
        return redirect(list_content)

    elif request.method == "GET":
        forms = Forms_contenido()
        context = {"forms":forms}
        return render (request, "products/new_content.html", context=context)

def search_content(request):
    search = request.GET['search']
    products = Contenido.objects.filter(name__icontains=search)
    context = {'products':products}
    return render(request, 'products/search_content.html', context=context)

def new_review(request):
    if request.method == "POST":
        form = Forms_review(request.POST)
        if form.is_valid():
            Reseña.objects.create(
                name = form.cleaned_data["name"],
                puntaje = form.cleaned_data["puntaje"],
                body = form.cleaned_data["body"],
                film = form.cleaned_data["film"]
            )
        return redirect(list_review)

    elif request.method == "GET":
        forms = Forms_review()
        context = {"forms":forms}
        return render (request, "products/new_review.html", context=context)