from django.utils import timezone
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


    # def validate_start(self, value):
    #     if value and value < timezone.now():
    #         raise serializers.ValidationError("Cannot schedule in the past.")
    #     return value

    def validate(self, data):
        instance = self.instance
        start = data.get('start_time', instance.start_time if instance else None)
        end = data.get('end_time', instance.end_time if instance else None)
        recurrence = data.get('recurrence', instance.recurrence if instance else 'none')
        interval = data.get('interval', instance.interval if instance else 1)

        if not start or not end:
            return data  # Let DRF catch missing field errors elsewhere

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
        # Check for overlaps
        # queryset = ScheduledRoutine.objects.filter(
        #     routine__user=instance.routine.user,
        #     start_time__time__lt=end.time(),
        #     end_time__time__gt=start.time()
        # ).exclude(id=instance.id)

        # for other in queryset:
        #     other_start = other.start_time
        #     other_end = other.end_time
        #     if not other_start or not other_end:
        #         continue
        #
        #     conflict = recurrences_conflict(
        #         new_rule=recurrence,
        #         existing_rule=other.recurrence,
        #         new_date=start,
        #         existing_date=other_start,
        #         new_interval=interval,
        #         existing_interval=other.interval
        #     )
        #
        #     if conflict:
        #         raise serializers.ValidationError("This event overlaps with another routine.")
        #
        # return data

    def get_rrule(self, obj):
        if obj.recurrence == 'none':
            return None

        dtstart = obj.start_time.strftime('%Y%m%dT%H%M%SZ')
        return {
            'freq': obj.recurrence.upper(),
            'dtstart': dtstart,
            'interval': obj.interval
        }

