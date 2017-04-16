from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'user', 'pub_date')
    list_display_links = ('id', 'title')
    list_filter = ('user', 'pub_date')
    search_fields = ('title', 'content')
    list_per_page = 25

admin.site.register(Post, PostAdmin)