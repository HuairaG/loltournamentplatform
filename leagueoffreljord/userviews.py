from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from .usermodels import *
from .userforms import *
from leagueoffreljord.userforms import *
from django.core.exceptions import ObjectDoesNotExist

class RegistroUsuario(CreateView):
    model = User
    template_name = 'index.html'
    form_class = UserForm
    success_url = reverse_lazy('home')


class ProfileView(View):
    template_name = 'profile/show.html'

    def get(self, request):
        profile_form = ProfileForm()
        try:
            profile = Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = None
        try:
            lol_profile = LolProfile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            lol_profile = None
        context = {
            'profile_form': profile_form,
            #'lol_profile_form': lol_profile_form,
            'profile': profile,
            'lol_profile': lol_profile,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        profile = None
        lol_profile = None
        if profile_form.is_valid():
            cleaned_data = profile_form.clean()
            profile = Profile(
                user=request.user,
                name=cleaned_data['name'],
                last_name=cleaned_data['last_name'],
                dni=cleaned_data['dni'],
                picture=cleaned_data['picture']
            )
            profile.save()
        context = {
            'profile': profile,
            'lol_profile': lol_profile,
        }
        return render(request, self.template_name, context)
