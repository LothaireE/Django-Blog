from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display: list[str]= ('title', 'published', 'author')
    date_hierarchy: str = 'published'
    search_fields: str = ('title', 'description')
