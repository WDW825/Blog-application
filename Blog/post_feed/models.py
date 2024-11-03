from django.db import models


class Post(models.Model):
    post_text = models.TextField()
    author = models.CharField(max_length=100)
    post_name = models.CharField(max_length=100, default='')
    post_date = models.DateField()
