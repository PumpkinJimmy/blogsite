from django.shortcuts import render
from .models import Article
from md_parse.parse import Parser, HtmlRenderer
# Create your views here.


def indexView(request):
    return render(request, 'myblog/index.html')

def articleView(request, id):
    art = Article.objects.get(id=id)
    parser = Parser()
    renderer = HtmlRenderer()
    content = renderer.render(parser.parse(art.content.replace('\r', '')))
    content = '<div class="md">' + content + '</div>'
    return render(request, 'myblog/article.html', context={'article': art, 'content':content})

def articleListView(request):
    arts = Article.objects.all()
    return render(request, 'myblog/article_list.html',
                  context={'articles':arts})

