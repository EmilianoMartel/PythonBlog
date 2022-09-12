from multiprocessing import context
from django.shortcuts import render, redirect
from products.models import Contenido, Reseña, Platform
from products.forms import Forms_contenido, Forms_review, Forms_platform
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from users.models import User_profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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
    content = Contenido.objects.filter(name__icontains=search)
    context = {'contents':content}
    return render(request, 'products/search_content.html', context=context)

class Delete_content(LoginRequiredMixin, DeleteView):
    model = Contenido
    template_name = 'products/delete_content.html'
    success_url = '/products/list-content/'

def new_review(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = Forms_review(request.POST)
            if form.is_valid():
                Reseña.objects.create(
                    name = form.cleaned_data["name"],
                    puntaje = form.cleaned_data["puntaje"],
                    body = form.cleaned_data["body"],
                    film = form.cleaned_data["film"],
                    author = request.user
                )
            return redirect(list_review)
        elif request.method == "GET":
            forms = Forms_review()
            context = {"forms":forms}
            return render (request, "products/new_review.html", context=context)
    else:
        return redirect('login')

class Delete_review(LoginRequiredMixin,DeleteView):
    model = Reseña
    template_name = 'products/delete_review.html'
    success_url = '/products/list-review/'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            messages.error(request, message='Usuario invalido. Solo el autor puede borrar la reseña.')
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs) #Entrega el formulario si salteó el if anterior

class New_platform(LoginRequiredMixin, CreateView):
    model = Platform
    template_name = 'products/new_platform.html'
    form_class = Forms_platform
    #fields = '__all__'
    success_url = '/products/list-platforms/'

class Delete_platform(LoginRequiredMixin, DeleteView):
    model = Platform
    template_name = 'products/delete_platform.html'
    success_url = '/products/list-platforms/'

def list_platforms(request):
    platforms = Platform.objects.all()
    context = {
        "platforms":platforms
    }
    return render(request, "products/platforms_list_card.html", context=context)

def index(request): #Lo que vimos en clase y las diapositivas está incompleto o mal - no se muestra la imagen
    return render(request, 'index.html')