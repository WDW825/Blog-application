# Generated by Django 5.1.1 on 2024-11-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_alter_theme_theme_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='theme_name_url',
            field=models.CharField(default='-', max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
