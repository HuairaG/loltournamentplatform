from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .usermodels import *

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'password1': 'Contrasena',
            'password2': 'Confirmar contrasena',
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        return cleaned_data

    def save(self):
        cleaned_data = super(ProfileForm, self).clean()

class LolProfileForm(forms.ModelForm):

    class Meta:
        model = LolProfile
        exclude = ('user', 'active', 'league', 'division')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LolProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(LolProfileForm, self).clean()
        return cleaned_data

    def save(self):
        cleaned_data = super(LolProfileForm, self).clean()
