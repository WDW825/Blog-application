from django.db import models


class Theme(models.Model):
    theme_name=models.CharField(max_length=50, unique=True)


#TODO: make function to generate proper theme name for url