from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag, Comment

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment) # 경로가 자동으로 wish_content로 지정됨

class BlogAdminSite(admin.AdminSite):
    site_url = '/admin/blog/'  # admin 사이트의 URL을 원하는 경로로 지정합니다.
blog_admin_site = BlogAdminSite(name='blogadmin')
blog_admin_site.register(Comment)  # 다른 설정들과 함께 Comment 모델을 등록해야 합니다.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

# chatGPT내용


blog_admin_site = BlogAdminSite(name='blogadmin')
blog_admin_site.register(Comment)  # 다른 설정들과 함께 Comment 모델을 등록해야 합니다.