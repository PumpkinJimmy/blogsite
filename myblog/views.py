from django.shortcuts import render, reverse, redirect
from .models import Article
from md_parse.parse import Parser, HtmlRenderer
from django.http.response import HttpResponse

# Create your views here.


def indexView(request):
    return render(request, 'myblog/index.html')

def articleView(request, id):
    art = Article.objects.get(id=id)
    if art.doctype == "markdown":
        parser = Parser()
        renderer = HtmlRenderer()
        content = renderer.render(parser.parse(art.content.replace('\r', '')))
        content = '<div class="md">' + content + '</div>'
        return render(request, 'myblog/article.html', context={'art': art, 'content':content})
    elif art.doctype == '' or art.doctype == 'plain':
        lines = art.content.split('\n')
        content = '<div class="text"><p>' + '</p><p>'.join(lines) + '</p></div>'
        return render(request, 'myblog/article.html', context={'art': art, 'content':content})
    else:
        raise Exception("Unknow doctype")
def articleListView(request):
    arts = Article.objects.all()
    return render(request, 'myblog/article_list.html',
                  context={'articles':arts})

def uploadView(request):
    if request.method == "GET":
        return render(request, 'myblog/upload.html')
    else:
        data = str(request.FILES['f'].read(), encoding="utf-8")
        lines = data.split('\n')
        brief_lcnt = min(4, len(lines))
        brief_ = '\n'.join(lines[:brief_lcnt])
        art = Article(title="test", content=data, brief=brief_)
        art.save()
        return redirect(reverse('article', kwargs={'id':art.pk}))


