from django.urls import path
from . import views
from . import userviews
from . import newsviews

app_name = 'api'
urlpatterns = [
    path('', views.home, name="home"),
    path('register', userviews.RegistroUsuario.as_view(), name="register"),
    path('profile', userviews.ProfileView.as_view(), name="profile"),
    path('profile/edit', userviews.ProfileUpdateView.as_view(), name="profile_edit"),
    path('profile/lol/edit', userviews.LolProfileUpdateView.as_view(), name="lol_profile_edit"),
    path('admin/article/new', newsviews.ArticleView.as_view(), name="article_create"),
    #path('admin/article/edit', newsviews.ArticleUpdateView.as_view(), name="article_edit"),
    path('admin/article/list', newsviews.ArticleListView.as_view(), name="article_list"),
]
