from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'timestamp')
    search_fields = ('title', 'slug')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
    prepopulated_fields = {'slug': ('title',)}