from django.contrib.auth.models import User
from django.db import models

def upload_location(instance, filename):
    return "%s/%s" %(instance.user.id, filename)

class LolProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=48)
    league = models.CharField(max_length=48)
    division = models.CharField(max_length=48, default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username + self.league + self.division + str(self.active)

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

    def __str__(self):
        return self.user.username
