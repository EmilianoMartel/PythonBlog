from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20) #Se podría mejorar con un regexfield que limite caracteres especiales, ejemplo: regex=r'^\+?1?\d{9,15}$'
    about = forms.CharField(max_length=250)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','about', 'email', 'password1', 'password2')

        #help_texts = {k:'' for k in fields} # Saca los comentarios de ayuda

