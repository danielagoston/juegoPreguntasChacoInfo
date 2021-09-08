from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('edad',)

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = UserChangeForm.Meta.fields 

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('usuario', 'email', 'edad',) # new

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('usuario', 'email', 'edad',) # new
