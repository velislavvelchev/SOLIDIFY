from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_type', 'description', 'min_habits_per_day')
    list_filter = ('category_type',)
    search_fields = ('category_type', 'description')
    ordering = ('category_type',)
    list_editable = ('min_habits_per_day',)



