from email.policy import default
from django.db import models
from products.models import Contenido
from django.contrib.auth.models import User
# Create your models here.


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True) 
    about = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='profile_image/',null=True, blank=True, default='profile_image/default.png')
    fav = models.ManyToManyField(Contenido, blank=True) #--PENDIENTE--# Uso esta tabla secundaria que crea automáticamente Django para guardar las películas que cada usuario marcó como favoritas. 

    def __str__(self):
        return self.user.username
