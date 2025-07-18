from django.utils import timezone
from rest_framework import serializers
from SOLIDIFY.schedule.models import ScheduledRoutine


class ScheduledRoutineCalendarSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='routine.routine_name', read_only=True)
    start = serializers.DateTimeField(source='start_time')
    end = serializers.DateTimeField(source='end_time', allow_null=True)

    class Meta:
        model = ScheduledRoutine
        fields = ['id', 'title', 'start', 'end']


    def validate_start(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError("Cannot schedule in the past.")
        return value