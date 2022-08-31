from django.urls import path
from users.views import login_request, register, show_profile, create_profile, Show_profile, Create_profile, Update_profile

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('show-profile/<int:pk>/', Show_profile.as_view(), name='Show_profile'),
    path('create-profile/', Create_profile.as_view(), name='Create_profile'),
    path('update-profile/<int:pk>/', Update_profile.as_view(), name='Update_profile'),
    path('show-profile2/', show_profile, name='show_profile'),
    path('create-profile2/<int:pk>/', create_profile, name='create_profile'),
    #path('profile/', show_profile, name='profile'),
]