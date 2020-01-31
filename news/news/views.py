from django.shortcuts import render
from datetime import datetime
from .models import Article


def index(request):
    context = {
        'current_date': datetime.now(),
        'title': 'Home'
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'current_date': datetime.now(),
        'title': 'About'
    }
    return render(request, 'about.html', context)

def news(request):

    populate_db()
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'current_date': datetime.now(),
        'title': 'News'
    }
    return render(request, 'news.html', context)

def populate_db():
    if Article.objects.count() == 0:
        Article(title = 'Diary of an african woman', content = "Let's just leave this for now").save()
        Article(title = 'Story of Twins', content = "Let's just leave this for now").save()
        Article(title = 'An eventful event', content = "Let's just leave this for now").save()