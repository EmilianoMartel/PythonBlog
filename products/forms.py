from django import forms

class Forms_contenido(forms.Form):
    name = forms.CharField(max_length=50)
    #categorias = [('P','Película'), ('S', 'Serie'), ('C', 'Corto')] comentados por ahora
    categorias = [('P','Película'), ('S', 'Serie'), ('C', 'Corto')]
    category = forms.ChoiceField(choices=categorias) 
    #genero similar a categorias si queremos agregarlo o podría ser una clase aparte para poder gestionarlas via panel de control
    score = forms.FloatField() #este quizás no tenga sentido tenerlo como campo en la base sino más bien que se calcule cada vez que se va a mostrar
    #created_date = forms.DateField()
    #modified_date = forms.DateTimeField()
    description = forms.CharField()
    image_url = forms.URLField()
