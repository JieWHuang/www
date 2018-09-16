from django.contrib import admin
from blog.models import Blog, Category, Tag, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
