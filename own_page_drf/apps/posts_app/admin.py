from django.contrib import admin

from .models import Post, PostImage, Comment


class PostAdmin(admin.ModelAdmin):
    pass


class PostImageAdmin(admin.ModelAdmin):
    pass

class PostCommnet(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
admin.site.register(Comment, PostCommnet)
