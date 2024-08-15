from django.contrib import admin
from blog.models import Category, Comments, Post
from blog.models import Users


class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Users)



