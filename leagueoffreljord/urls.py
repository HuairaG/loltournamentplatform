from django.urls import path
from . import views
from . import userviews
from . import newsviews

app_name = 'api'
urlpatterns = [
    path('', views.home, name="home"),
    path('register', userviews.RegistroUsuario.as_view(), name="register"),
    path('profile', userviews.ProfileView.as_view(), name="profile"),
    path('profile/edit_profile', userviews.ProfileUpdateView.as_view(), name="profile_edit"),
    path('profile/edit_lol_profile', userviews.LolProfileUpdateView.as_view(), name="lol_profile_edit"),
    path('news/editor', newsviews.ArticleView.as_view(), name="article_editor"),
]
