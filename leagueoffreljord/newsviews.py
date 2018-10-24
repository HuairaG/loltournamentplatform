from .newsmodels import *
from django.views.generic import View, UpdateView, ListView
from django.shortcuts import render, redirect
from .newsforms import *
from django.contrib import messages
from django.utils import timezone

def article_save(request, article_form, article=None):
    cleaned_data = article_form.clean()
    if article is None:
        article = Article(
            author=request.user,
            title=cleaned_data['title'],
            content=cleaned_data['content'],
            draft=cleaned_data['draft'],
        )
    else:
        article.author = request.user
        article.title = cleaned_data['title']
        article.content = cleaned_data['content']
        article.draft = cleaned_data['draft']
    article.save()
    return article

class ArticleView(View):
    template_name = 'news/admin/createArticle.html'

    def get(self, request):
        article_form = ArticleForm()
        context = {
            'article_form': article_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            cleaned_data = article_form.clean()
            article_save(request, article_form)
            messages.success(request, 'Articulo guardado exitosamente')
        else:
            messages.error(request, 'Ocurrio un error')
        return redirect('api:profile')

class ArticleListView(ListView):
    model = Article
    page_kwarg = 'page'
    paginate_by = 30
    ordering = 'last_modified'
    template_name = 'news/admin/listArticles.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['now'] = timezone.now()
            return context

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content', 'draft')
    template_name = 'news/admin/updateArticle.html'
