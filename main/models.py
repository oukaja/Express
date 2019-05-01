from django.db import models

# Create your models here.

class Article(models.Model):
    journal = models.CharField(max_length = 50)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 60)
    link = models.CharField(max_length = 500)
    photo = models.CharField(max_length = 500)