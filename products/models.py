from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contenido(models.Model):
    name = models.CharField(max_length=50)
    categorias = [('P','Película'), ('S', 'Serie'), ('C', 'Corto')]
    category = models.CharField(max_length=1,choices=categorias)
    #genero similar a categorias si queremos agregarlo o podría ser una clase aparte para poder gestionarlas via panel de control
    score = models.FloatField() #este campo debería darse de baja y reemplazar por un cálculo dinámico según las votaciones de usuarios cargadas en reseñas.
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField( auto_now=True)
    description = models.TextField(null=True)
    image_url = models.URLField(default="https://image.shutterstock.com/image-vector/photo-album-picture-collection-line-260nw-256926565.jpg")
    def __str__(self):
        return self.name + ' - ' + self.get_category_display() #devuelve el 2do objeto de la tupla en lugar del primero --> guarda 1 letra pero muestra el nombre completo

class Platform(models.Model): #Lo doy de alta como clase para poder filtrar contenido en base a plataformas de manera fácil
    name = models.CharField(max_length=50, unique=True) 
    description = models.TextField(null=True)
    image_url = models.URLField(default="https://image.shutterstock.com/image-vector/photo-album-picture-collection-line-260nw-256926565.jpg")
    contains = models.ManyToManyField(Contenido, blank=True) #peliculas que están en cada plataforma
    def __str__(self):
        return self.name

class Reseña(models.Model):
    name = models.CharField(max_length=40)
    film = models.ForeignKey(
        'Contenido',
        on_delete=models.CASCADE,
    )
    body = models.TextField(null=True)
    puntaje = models.FloatField()
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING, default=5)
    def __str__(self):
        return self.name + ' - ' + self.film  
