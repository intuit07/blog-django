from django.db import models


# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slag = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)
