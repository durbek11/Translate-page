from django.db import models
from django.urls import reverse

class TranslatePage(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('translate:home', kwargs={'slug': self.slug})