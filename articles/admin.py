from django.contrib import admin

# Register your models here.

from .models import Article, Comment

class CommentInLine(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine,]

admin.site.register(Article)
admin.site.register(Comment)