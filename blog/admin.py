from django.contrib import admin
from .models import Post, CommentPost

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'created')


admin.site.register(Post, PostAdmin)
admin.site.register(CommentPost, CommentAdmin)
