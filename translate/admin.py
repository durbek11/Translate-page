from django.contrib import admin
from .models import *

@admin.register(TranslatePage)
class Translate(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
