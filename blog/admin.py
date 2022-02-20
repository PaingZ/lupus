from django.contrib import admin
from .models import Post

class List(admin.ModelAdmin):
    list_display = ('title','author','date','status')
    search_fields = ('title',)

admin.site.register(Post, List)

