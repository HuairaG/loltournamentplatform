from django.contrib.auth.models import User
from django.db import models

def upload_location(instance, filename):
    return "%s/%s" %(instance.user.id, filename)

class Nickname(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=48)
    active = models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    dni = models.PositiveIntegerField()
    picture = models.ImageField(
                upload_to=upload_location,
                null=True,
                blank=True,
    )
    league = models.CharField(max_length=80, blank=True)
    nickname = models.CharField(max_length=80, blank=True)
