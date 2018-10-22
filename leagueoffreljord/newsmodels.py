from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250,null=True)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
