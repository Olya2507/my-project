from django.views.generic import ListView, DetailView
from .models import Article



class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

