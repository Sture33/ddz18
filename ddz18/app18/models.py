from django.db import models
from django.utils.text import slugify


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f"{self.name}-{self.surname}")
        return super().save(force_insert, force_update, using, update_fields)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, null=True,on_delete=models.SET_NULL)
    genre = models.CharField(max_length=255)
    raiting = models.FloatField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f"{self.title}-{self.author}-{self.genre}")
        return super().save(force_insert, force_update, using, update_fields)