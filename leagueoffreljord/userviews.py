from leagueoffreljord.userforms import UserForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class RegistroUsuario(CreateView):
    model = User
    template_name = 'login/register.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
