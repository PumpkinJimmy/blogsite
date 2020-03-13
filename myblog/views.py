from django.shortcuts import render, reverse, redirect
from .models import Article, Category, Tag
from md_parse.parse import Parser, HtmlRenderer, ContentsParser, ContentsRenderer
from django.http.response import HttpResponse
import django.contrib.auth as auth

# Create your views here.


def indexView(request):
    return render(request, 'myblog/index.html', context={'request':request})

def articleView(request, id, upload_success=False):
    art = Article.objects.get(id=id)
    if art.doctype == "markdown":
        parser = Parser()
        renderer = HtmlRenderer()
        ast = parser.parse(art.content.replace('\r', ''))
        cs = ContentsParser().parse(ast)
        cs = ContentsRenderer().render(cs)
        content = renderer.render(ast)
        content = '<div class="md">' + content + '</div>'
        return render(request, 'myblog/article.html', context={'request':request, 'cs':cs, 'ast': ast, 'art': art, 'content':content, 'success':upload_success})
    elif art.doctype == '' or art.doctype == 'plain':
        lines = art.content.split('\n')
        content = '<div class="text"><p>' + '</p><p>'.join(lines) + '</p></div>'
        return render(request, 'myblog/article.html', context={
            'request':request, 'art': art, 'content':content, 'success':upload_success})
    else:
        raise Exception("Unknow doctype")
def articleListView(request):
    arts = Article.objects.order_by('-update_date')
    return render(request, 'myblog/article_list.html',
                  context={'articles':arts, 'request':request})

def uploadView(request):
    if not request.user.is_authenticated:
        return HttpResponse("无权访问")
    if request.method == "GET":
        return render(request, 'myblog/upload.html', context={'request':request})
    else:
        data = str(request.FILES['file'].read(), encoding="utf-8")
        # lines = data.split('\n')
        # brief_lcnt = min(4, len(lines))
        # brief_ = '\n'.join(lines[:brief_lcnt])
        brief_ = request.POST['brief']
        category = Category.objects.get(name=request.POST['category'])
        art = Article(
            title=request.POST['title'], content=data, brief=brief_, category=category, doctype=request.POST['doctype'])
        art.save()
        return articleView(request, art.pk, True)
        # return redirect('article', id=art.pk)

def tagsView(request):
    return render(request, "myblog/tags.html", context={
        'tags': Tag.objects.all()
    })


