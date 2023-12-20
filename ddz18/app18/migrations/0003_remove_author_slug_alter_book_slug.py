# Generated by Django 5.0 on 2023-12-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app18', '0002_author_slug_alter_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
