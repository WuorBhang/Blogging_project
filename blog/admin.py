from django.contrib import admin
from .models import Post, Category, Tag, Comment, Like


# Customize Post display in the admin panel
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date', 'date_created')
    list_filter = ('category', 'author', 'published_date')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-date_created',)

# Customize Comment display in the admin panel
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'date_created')
    search_fields = ('user__username', 'post__title', 'content')
    list_filter = ('post', 'date_created')

# Customize Like display in the admin panel
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('user__username', 'post__title')



# Register models with the admin site
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
