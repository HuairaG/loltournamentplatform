from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    #categories = models.ManyToManyField("Category", blank=True) # Quizas en una implementacion futura.
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ('title',)

    def __str__(self):
        return self.title
