from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30)
    father = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    brief = models.CharField(max_length=400)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    doctype = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.title
