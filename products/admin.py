from django.contrib import admin
from products.models import Producto

# Register your models here.
@admin.register(Producto)
class Producto_admin(admin.ModelAdmin):
    list_display = [
    'name'
    ,'price'
    ,'created_date'
    ,'modified_date'
    ,'description'
    ,'active'
    ,'image_url'
    ]