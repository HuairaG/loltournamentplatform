from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from .usermodels import *
from .userforms import *
from leagueoffreljord.userforms import *
from django.core.exceptions import ObjectDoesNotExist
from .riotAPI import RiotAPI
import leagueoffreljord.riotConstants as Consts

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
        if profile is None:
            img = "https://2.bp.blogspot.com/-lHLm8cAZH6U/WO56Z0mflyI/AAAAAAAAiNM/tOUpYVq5L8MLymkLOOJ2TX_Fr9aqwdfWwCLcB/s1600/8fc65aa22d388770.jpg"
        else:
            img = profile.picture.url
        try:
            lol_profile = LolProfile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            lol_profile = None
        context = {
            'img': img,
            'profile_form': profile_form,
            #'lol_profile_form': lol_profile_form,
            'profile': profile,
            'lol_profile': lol_profile,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        lol_profile_form = LolProfileForm(request.POST)
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
        else:
            try:
                profile = Profile.objects.get(user=request.user)
            except ObjectDoesNotExist:
                profile = None
        if profile is None:
            img = "https://2.bp.blogspot.com/-lHLm8cAZH6U/WO56Z0mflyI/AAAAAAAAiNM/tOUpYVq5L8MLymkLOOJ2TX_Fr9aqwdfWwCLcB/s1600/8fc65aa22d388770.jpg"
        else:
            img = profile.picture.url
        if lol_profile_form.is_valid():
            league = 'Unranked'
            division = ''
            cleaned_data = lol_profile_form.clean()
            api = RiotAPI(Consts.KEY)
            summoner = api.get_summoner_by_name(cleaned_data['nickname'])
            league_data = api.get_league_by_id(summoner['id'])
            for queue_data in league_data:
                if queue_data['queueType'] == Consts.QUEUE['solo']:
                    league = queue_data['tier']
                    division = queue_data['rank']
                    print(league)
            lol_profile = LolProfile(
                user=request.user,
                nickname=cleaned_data['nickname'],
                league=league,
                division=division,
                active=True
            )
            lol_profile.save()
        else:
            try:
                lol_profile = LolProfile.objects.get(user=request.user)
            except ObjectDoesNotExist:
                lol_profile = None
        context = {
            'profile': profile,
            'lol_profile': lol_profile,
            'img': img,
        }
        return render(request, self.template_name, context)
