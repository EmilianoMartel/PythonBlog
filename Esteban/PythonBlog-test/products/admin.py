from django.contrib import admin
from products.models import Producto, User, Contenido

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

@admin.register(User)
class User_admin(admin.ModelAdmin):
    list_display = [
    'name'
    ,'mail'
    ]

@admin.register(Contenido)
class Contenido_admin(admin.ModelAdmin):
    list_display = [
    'name'
    ,'category'
    ,'score'
    ,'modified_date'
    ,'created_date'
    ,'description'
    ,'image_url'
    ]