from django.contrib import admin
from . models import News, Category

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name','available',)
    list_filter = ('available',)
    search_fields = ('name','description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}