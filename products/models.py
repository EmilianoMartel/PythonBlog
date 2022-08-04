from email.policy import default
from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField( auto_now=True)
    description = models.TextField()
    active =  models.BooleanField(default=True)
    image_url =  models.URLField()
