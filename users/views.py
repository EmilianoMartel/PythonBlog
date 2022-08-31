from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from users.forms import User_registration_form
from users.models import User_profile

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'¡Bienvenido {username}!'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Usuario o contraseña incorrecto', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})

def show_profile(request):
    if request.user.is_authenticated:
        try:
            u = User_profile.objects.get(id=request.user.id)
            print(u, type(u))
            context = {'user': u}
            return render(request, 'users/profile.html', context)
        except:
            return redirect(create_profile)

def create_profile(request):
    if request.user.is_authenticated:
        u = User_profile.objects.get(id=request.user.id)
        context = {'user': u}
        return render(request, 'users/profile.html', context)

class Show_profile(LoginRequiredMixin,DetailView):
    model = User_profile
    template_name = 'users/profile.html'

class Create_profile(LoginRequiredMixin,CreateView):
    model = User_profile
    template_name = 'users/create_profile.html'
    fields = '__all__'
    success_url = 'users/profile.html'

class Update_profile(LoginRequiredMixin,UpdateView):
    model = User_profile
    fields = '__all__'
    success_url = 'users/profile.html'