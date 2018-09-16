from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from .usermodels import *
from leagueoffreljord.userforms import *

class RegistroUsuario(CreateView):
    model = User
    template_name = 'index.html'
    form_class = UserForm
    success_url = reverse_lazy('home')

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'profile/edit.html'

class ProfileView(View):
    template_name = 'profile/show.html'

    def get(self, request):
        pass

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente.')
            return render(request, self.template_name)
