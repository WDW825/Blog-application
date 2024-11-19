from django.db import models


class Theme(models.Model):
    theme_name=models.CharField(max_length=50, unique=True)
    theme_name_url = models.CharField(max_length=30, unique=True)




#TODO: make function to generate proper theme name for url