from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserEditForm(UserCreationForm):

    imagen      = forms.ImageField(label='Foto')
    nickname    = forms.CharField(label='NickName',max_length=30)
    descripcion = forms.CharField(label='Acerca de mi',max_length=300)
    linkWeb     = forms.URLField(label='Link a tu pagina Web')
    email       = forms.EmailField(label='Email')
    password1   = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2   = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)    
    

    class Meta:
        model = User
        fields = ['imagen', 'nickname', 'descripcion', 'linkWeb','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
