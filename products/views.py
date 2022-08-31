from django.shortcuts import render, redirect
from products.models import Contenido, Reseña, Platform
from products.forms import Forms_contenido, Forms_review, Forms_platform
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from users.models import User_profile
from django.urls import reverse


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

def delete_content(DeleteView):
    model = Contenido
    templete_name = "products/delete_content.html"
    def get_success_url(self):
        return reverse("list_content")

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

def delete_review(DeleteView):
    model = Reseña
    template_name = "products/delete_review.html"

    def get_success_url(self):
        return reverse("profucts/list_review.html")

"""def new_platform(request): #No guarda la data de la relación y tira diversos errores. Uso la vista basada en clase que funciona perfecto.
    if request.method == "POST":
        form = Forms_platform(request.POST)
        if form.is_valid():
            Platform.objects.create(
                name = form.cleaned_data["name"],
                description = form.cleaned_data["description"],
                image_url = form.cleaned_data["image_url"],
            )
            #selected_categories = form.cleaned_data.get('category') #returns list of all selected categories e.g. ['Sports','Adventure']
            selected_content = form.cleaned_data["contains"]
            print(selected_content)
            for title in selected_content:
                print(title.id)
                relacion = Contenido.objects.get(id=title.id) #get object by title i.e I declared unique for title under Category model
                Platform.contains.add(relacion) #now add each category object to the saved form object
            context = { 'message' : 'creación exitosa'}
        return render(request, "products/new_platform.html", context=context)

    elif request.method == "GET":
        forms = Forms_platform()
        context = {"forms":forms}
        return render(request, "products/new_platform.html", context=context)
"""

class New_platform(CreateView):
    model = Platform
    template_name = 'products/new_platform.html'
    #form_class = Forms_platform
    fields = '__all__'
    success_url = '/products/list-platforms/'

class Delete_platform(DeleteView):
    model = Platform
    template_name = 'products/delete_platform.html'
    success_url = '/products/list-platforms/'

def list_platforms(request):
    platforms = Platform.objects.all()
    context = {
        "platforms":platforms
    }
    return render(request, "products/platforms_list_card.html", context=context)

def index(request): #Lo que vimos en clase y las diapositivas está incompleto o mal
    return render(request, 'index.html')