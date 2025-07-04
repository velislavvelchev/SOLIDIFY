from django.contrib import admin
from .models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'habit_name', 'dopamine_type', 'category', 'is_completed', 'priority', 'user', 'created_at')
    list_filter = ('dopamine_type', 'category', 'is_completed', 'priority')
    search_fields = ('habit_name', 'notes')
    ordering = ('-created_at',)
    list_editable = ('is_completed', 'priority')
