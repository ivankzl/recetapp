# Generated by Django 3.0.5 on 2020-05-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200503_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, verbose_name='slug'),
        ),
    ]
