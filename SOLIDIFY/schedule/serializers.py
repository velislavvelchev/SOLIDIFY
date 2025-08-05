from rest_framework import serializers
from SOLIDIFY.schedule.models import ScheduledRoutine
from SOLIDIFY.schedule.utils import recurrences_conflict
from SOLIDIFY.schedule.validators import ScheduledRoutineValidator


class ScheduledRoutineCalendarSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='routine.routine_name', read_only=True)
    start = serializers.DateTimeField(source='start_time')
    end = serializers.DateTimeField(source='end_time', allow_null=True)
    rrule = serializers.SerializerMethodField()

    class Meta:
        model = ScheduledRoutine
        fields = ['id', 'title', 'start', 'end', 'rrule']



    def validate(self, data):
        instance = self.instance
        start = data.get('start_time', instance.start_time if instance else None)
        end = data.get('end_time', instance.end_time if instance else None)
        recurrence = data.get('recurrence', instance.recurrence if instance else 'none')
        interval = data.get('interval', instance.interval if instance else 1)

        if not start or not end:
            return data

        validator = ScheduledRoutineValidator(
            user=instance.routine.user,
            start=start,
            end=end,
            recurrence=recurrence,
            interval=interval,
            instance=instance
        )
        errors = validator.validate()

        if errors:
            # Raise the first relevant error
            raise serializers.ValidationError(dict(errors) if any(e[0] for e in errors) else errors[0][1])

        return data


    def get_rrule(self, obj):
        if obj.recurrence == 'none':
            return None

        dtstart = obj.start_time.strftime('%Y%m%dT%H%M%SZ')
        return {
            'freq': obj.recurrence.upper(),
            'dtstart': dtstart,
            'interval': obj.interval
        }

