from django.views.generic import CreateView, View, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .usermodels import *
from .userforms import *
from leagueoffreljord.userforms import *
from django.core.exceptions import ObjectDoesNotExist
from .riotAPI import RiotAPI
import leagueoffreljord.riotConstants as Consts
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .useraux import *

class RegistroUsuario(CreateView):
    model = User
    template_name = 'index.html'
    form_class = UserForm
    success_url = reverse_lazy('home')


class ProfileView(View):
    template_name = 'profile/show.html'

    @method_decorator(login_required(login_url='api:home', redirect_field_name='api:profile'))
    def get(self, request):
        profile_form = ProfileForm()
        profile = get_profile_from_user_or_none(request.user)
        lol_profile = get_lolprofile_from_user_or_none(request.user)
        if profile is None:
            img = "https://2.bp.blogspot.com/-lHLm8cAZH6U/WO56Z0mflyI/AAAAAAAAiNM/tOUpYVq5L8MLymkLOOJ2TX_Fr9aqwdfWwCLcB/s1600/8fc65aa22d388770.jpg"
        else:
            img = profile.picture.url
        context = {
            'img': img,
            'profile_form': profile_form,
            #'lol_profile_form': lol_profile_form,
            'profile': profile,
            'lol_profile': lol_profile,
        }
        return render(request, self.template_name, context)

    @method_decorator(login_required(login_url='api:home', redirect_field_name='api:profile'))
    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        lol_profile_form = LolProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_save(request, profile_form)
            messages.success(request, 'Perfil actualizado exitosamente')
        else:
            profile = get_profile_from_user_or_none(request.user)
        if profile is None:
            img = "https://2.bp.blogspot.com/-lHLm8cAZH6U/WO56Z0mflyI/AAAAAAAAiNM/tOUpYVq5L8MLymkLOOJ2TX_Fr9aqwdfWwCLcB/s1600/8fc65aa22d388770.jpg"
        else:
            img = profile.picture.url
        if lol_profile_form.is_valid():
            lol_profile = lolprofile_save(request, lol_profile_form)
        else:
            lol_profile = get_lolprofile_from_user_or_none(request.user)
        context = {
            'profile': profile,
            'lol_profile': lol_profile,
            'img': img,
        }
        return render(request, self.template_name, context)

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile/profile_edit.html'

    @method_decorator(login_required(login_url='api:home', redirect_field_name='api:profile_edit'))
    def get(self, request):
        profile_form = ProfileForm()
        return render(request, self.template_name, {'profile_form': profile_form})

    @method_decorator(login_required(login_url='api:home', redirect_field_name='api:profile_edit'))
    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = get_profile_from_user_or_none(request.user)
            profile = profile_save(request, profile_form, profile)
            messages.success(request, 'Perfil actualizado exitosamente')
        else:
            messages.error(request, 'El formulario es invalido, por favor ingrese los datos nuevamente', extra_tags='update-profile-error')
        return redirect('api:profile')

class LolProfileUpdateView(UpdateView):
    model = LolProfile
    template_name = 'profile/lol_profile_edit.html'

    @method_decorator(login_required(login_url='api:home', redirect_field_name='api:lol_profile_edit'))
    def get(self, request):
        lol_profile_form = LolProfileForm()
        return render(request, self.template_name, {'lol_profile_form': lol_profile_form})

    @method_decorator(login_required(login_url='api:home', redirect_field_name='api:lol_profile_edit'))
    def post(self, request):
        lol_profile_form = LolProfileForm(request.POST)
        if lol_profile_form.is_valid():
            lol_profile = get_lolprofile_from_user_or_none(request.user)
            lol_profile.active = False
            lol_profile.save()
            lol_profile = lolprofile_save(request, lol_profile_form)
            messages.success(request, 'Perfil de invocador actualizado exitosamente')
        else:
            messages.error(request, 'El formulario es invalido, por favor ingrese los datos nuevamente', extra_tags='update-lol-profile-error')
        return redirect('api:profile')
