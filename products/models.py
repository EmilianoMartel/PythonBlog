from django.db import models

# Create your models here.
class Contenido(models.Model):
    name = models.CharField(max_length=50)
    categorias = [('P','Película'), ('S', 'Serie'), ('C', 'Corto')]
    category = models.CharField(max_length=1,choices=categorias)
    #genero similar a categorias si queremos agregarlo o podría ser una clase aparte para poder gestionarlas via panel de control
    score = models.FloatField() #este quizás no tenga sentido tenerlo como campo en la base sino más bien que se calcule cada vez que se va a mostrar
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateTimeField( auto_now=True)
    description = models.TextField(null=True)
    image_url = models.URLField(default="https://image.shutterstock.com/image-vector/photo-album-picture-collection-line-260nw-256926565.jpg")
    def __str__(self):
        return self.name + ' - ' + self.get_category_display()

class User(models.Model): #La idea es agregarle usuarios y que puedan marcar productos como favoritos dentro del listado de productos y en una URL específica puedan ver esa lista
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mail = models.EmailField()
    fav = models.ManyToManyField(Contenido) #favoritos

class Platform(models.Model): #Lo doy de alta como clase para poder filtrar contenido en base a plataformas de manera fácil
    name = models.CharField(max_length=50) 
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
    def __str__(self):
        return self.name + ' - ' + self.film  


"""    
class Favorito(models.Model):
    user_id = IntegerField
    producto_id = IntegerField
"""