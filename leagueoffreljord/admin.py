from django.contrib import admin
from .usermodels import *
from .newsmodels import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(LolProfile)
admin.site.register(Article)
