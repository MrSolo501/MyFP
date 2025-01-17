from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Article


# Create your views here.
def home(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})