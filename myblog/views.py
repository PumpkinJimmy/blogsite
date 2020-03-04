from django.shortcuts import render, reverse, redirect
from .models import Article, Category
from md_parse.parse import Parser, HtmlRenderer
from django.http.response import HttpResponse

# Create your views here.


def indexView(request):
    return render(request, 'myblog/index.html')

def articleView(request, id, upload_success=False):
    art = Article.objects.get(id=id)
    if art.doctype == "markdown":
        parser = Parser()
        renderer = HtmlRenderer()
        content = renderer.render(parser.parse(art.content.replace('\r', '')))
        content = '<div class="md">' + content + '</div>'
        return render(request, 'myblog/article.html', context={'art': art, 'content':content, 'success':upload_success})
    elif art.doctype == '' or art.doctype == 'plain':
        lines = art.content.split('\n')
        content = '<div class="text"><p>' + '</p><p>'.join(lines) + '</p></div>'
        return render(request, 'myblog/article.html', context={'art': art, 'content':content, 'success':upload_success})
    else:
        raise Exception("Unknow doctype")
def articleListView(request):
    arts = Article.objects.order_by('-update_date')
    return render(request, 'myblog/article_list.html',
                  context={'articles':arts})

def uploadView(request):
    if request.method == "GET":
        return render(request, 'myblog/upload.html')
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


