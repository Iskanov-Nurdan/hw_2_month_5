from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
