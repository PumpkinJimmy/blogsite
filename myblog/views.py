from django.shortcuts import render
from .models import Article
# Create your views here.


def indexView(request):
    return render(request, 'myblog/index.html')

def articleView(request, id):
    art = Article.objects.get(id=id)

    return render(request, 'myblog/article.html', context={'article': art})

def articleListView(request):
    arts = Article.objects.all()
    return render(request, 'myblog/article_list.html',
                  context={'articles':arts})

