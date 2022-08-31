from django.urls import path
from users.views import login_request, register, show_profile, create_profile, Show_profile, Create_profile, Update_profile, Delete_profile

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('show-profile/<int:pk>/', Show_profile.as_view(), name='Show_profile'),
    path('update-profile/<int:pk>/', Update_profile.as_view(), name='Update_profile'),
    
    #-# Para evitar errores, no permito borrar un perfil, ya que trae errores con las imágenes, haciendo que el html no se renderice o django devuelva errores.
    #-# Como el perfil se crea automáticamente, tampoco necesito las vistas para generarlo. Las dejo para no tener que romper todo lo que ya estaba hecho y evitar errores por imports, etc
    #path('create-profile/', Create_profile.as_view(), name='Create_profile'),
    #path('show-profile2/', show_profile, name='show_profile'),
    #path('create-profile2/', create_profile, name='create_profile'),
    #path('delete-profile/<int:pk>/', Delete_profile.as_view(), name='Delete_profile'),
    #path('profile/', show_profile, name='profile'),
]