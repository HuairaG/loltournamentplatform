from django import forms
from .newsmodels import *
from tinymce import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class ArticleForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Article
        exclude = ('author', 'created_at', 'last_modified',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        return cleaned_data

    def save(self):
        cleaned_data = super(ArticleForm, self).save()
