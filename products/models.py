from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField( auto_now=True)
    description = models.TextField(null=True)
    active =  models.BooleanField(default=True)
    image_url = models.URLField(default="https://nayemdevs.com/wp-content/uploads/2020/03/default-product-image.png")
    
