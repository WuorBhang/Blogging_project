from django.contrib import admin
from .models import Post, Category, Tag, Comment, Like



# Register models with the admin site
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)
