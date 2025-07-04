from django.contrib import admin
from .models import ScheduledRoutine

@admin.register(ScheduledRoutine)
class ScheduledRoutineAdmin(admin.ModelAdmin):
    list_display = ('id', 'routine', 'start_time', 'end_time')
    list_filter = ('routine', 'start_time')
    search_fields = ('routine__routine_name',)
    ordering = ('-start_time',)
    date_hierarchy = 'start_time'
