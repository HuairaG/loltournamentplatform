from .newsmodels import *
from django.views.generic import CreateView, View, UpdateView
from django.shortcuts import render, redirect
from .newsforms import *

class ArticleView(View):
    template_name = 'news/editor.html'

    def get(self, request):
        article_form = ArticleForm()
        context = {
            'article_form': article_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass
