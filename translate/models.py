from django.db import models
from django.urls import reverse

class TranslatePage(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    me = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
