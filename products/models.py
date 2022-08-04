from pyexpat import model
from django.db import models

# Create your models here.
class Producto(models.Model):
    #id = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField( auto_now=True)
    description = models.TextField(null=True)
    active =  models.BooleanField(default=True)
    image_url = models.URLField(default="https://image.shutterstock.com/image-vector/photo-album-picture-collection-line-260nw-256926565.jpg")
    

class User(models.Model): #La idea es agregarle usuarios y que puedan marcar productos como favoritos dentro del listado de productos y en una URL específica puedan ver esa lista
    #id = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    favs = models.ManyToManyField(Producto) #favoritos

"""    
class Favorito(models.Model):
    user_id = IntegerField
    producto_id = IntegerField
"""