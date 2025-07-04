from django.contrib import admin
from .models import Routine

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('id', 'routine_name', 'category', 'user')
    list_filter = ('category', 'user')
    search_fields = ('routine_name',)
    ordering = ('routine_name',)
    filter_horizontal = ('habits',)
