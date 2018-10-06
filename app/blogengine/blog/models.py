from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slag = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slag': self.slag})

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slag = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
