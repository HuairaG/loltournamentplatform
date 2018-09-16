from django.urls import path
from . import views
from . import userviews

app_name = 'api'
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', userviews.RegistroUsuario.as_view(), name="register"),
    path('profile/edit', userviews.ProfileCreateView.as_view(), name="edit_profile"),
    path('profile', userviews.ProfileView.as_view(), name="show_profile"),
]
