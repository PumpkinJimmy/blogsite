from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.indexView),
    url(r'^article/$', views.articleListView),
    url(r'^article/(?P<id>[0-9]+)$', views.articleView, name="article")
]
