from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = '02 Categorías'

    def __str__(self):
        return self.title

