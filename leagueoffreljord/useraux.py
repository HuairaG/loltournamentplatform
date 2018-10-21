from .usermodels import *
from .userforms import *
from .riotAPI import RiotAPI
import leagueoffreljord.riotConstants as Consts
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# This module provides some auxiliary functions needed by the user views.

def profile_save(request, profile_form, profile=None):
    cleaned_data = profile_form.clean()
    if profile is None:
        profile = Profile(
            user=request.user,
            name=cleaned_data['name'],
            last_name=cleaned_data['last_name'],
            dni=cleaned_data['dni'],
            picture=cleaned_data['picture']
        )
    else:
        profile.user = request.user
        profile.name = cleaned_data['name']
        profile.last_name = cleaned_data['last_name']
        profile.dni = cleaned_data['dni']
        profile.picture = cleaned_data['picture']
    profile.save()
    return profile

def lolprofile_save(request, lol_profile_form, lol_profile=None):
    league = 'Unranked'
    division = ''
    cleaned_data = lol_profile_form.clean()
    api = RiotAPI(Consts.KEY)
    summoner = api.get_summoner_by_name(cleaned_data['nickname'])
    try:
        league_data = api.get_league_by_id(summoner['id'])
    except:
        messages.error(request, 'El invocador no existe', extra_tags='create-lol-profile-error')
        return None
    messages.success(request, 'Perfil de invocador actualizado exitosamente')
    for queue_data in league_data:
        if queue_data['queueType'] == Consts.QUEUE['solo']:
            league = queue_data['tier']
            division = queue_data['rank']
    lol_profile = LolProfile(
        user=request.user,
        nickname=cleaned_data['nickname'],
        league=league,
        division=division,
        active=True
    )
    lol_profile.save()
    return lol_profile

def get_profile_from_user_or_none(user):
    try:
        profile = Profile.objects.get(user=user)
    except ObjectDoesNotExist:
        profile = None
    return profile

def get_lolprofile_from_user_or_none(user):
    try:
        lol_profile = LolProfile.objects.get(user=user, active=True)
    except ObjectDoesNotExist:
        lol_profile = None
    return lol_profile
