from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField( auto_now=True)
    description = models.TextField(null=True)
    active =  models.BooleanField(default=True)
    image_url = models.URLField(default="https://image.shutterstock.com/image-vector/photo-album-picture-collection-line-260nw-256926565.jpg")
    
