from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30)
    father = models.ForeignKey('self', models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=200)
    brief = models.CharField(max_length=400)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
