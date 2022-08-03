from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()
    seller = models.CharField(max_length=40)

    def __str__(self):
        return self.name
