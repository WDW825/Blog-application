from django.db import models

class Post(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    post_date = models.DateField()
