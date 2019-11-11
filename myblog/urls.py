from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.indexView, name="index"),
    url(r'^article/$', views.articleListView, name="article_list"),
    url(r'^article/(?P<id>[0-9]+)$', views.articleView, name="article"),
    url(r'^upload/$', views.uploadView, name="upload")
]
