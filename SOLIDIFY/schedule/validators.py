from django.utils import timezone
from SOLIDIFY.schedule.models import ScheduledRoutine
from SOLIDIFY.schedule.utils import recurrences_conflict


class ScheduledRoutineValidator:
    def __init__(self, *, user, start, end, recurrence, interval, instance=None):
        self.user = user
        self.start = start
        self.end = end
        self.recurrence = recurrence or 'none'
        self.interval = interval or 1
        self.instance = instance

    def validate(self):
        errors = []

        # Validate: start < end
        if self.start and self.end and self.start >= self.end:
            errors.append(("start_time", "Start time must be before end time."))
            errors.append(("end_time", "End time must be after start time."))
            return errors

        # Validate: can't schedule in the past
        if self.start and self.start < timezone.now():
            errors.append(("start_time", "You cannot schedule a routine in the past."))
            return errors

        if self.start and self.end:
            # Non-recurring direct overlap check
            conflicts = ScheduledRoutine.objects.filter(
                routine__user=self.user,
                start_time__lt=self.end,
                end_time__gt=self.start,
            )
            if self.instance and self.instance.pk:
                conflicts = conflicts.exclude(pk=self.instance.pk)

            if conflicts.exists():
                errors.append((None, "This routine overlaps with another scheduled routine."))
                return errors

            # Recurrence-based overlap check
            possible_conflicts = ScheduledRoutine.objects.filter(
                routine__user=self.user,
                start_time__time__lt=self.end.time(),
                end_time__time__gt=self.start.time()
            )
            if self.instance and self.instance.pk:
                possible_conflicts = possible_conflicts.exclude(pk=self.instance.pk)

            for conflict in possible_conflicts:
                if self.recurrence == 'none' and conflict.recurrence == 'none':
                    if self.start.date() != conflict.start_time.date():
                        continue

                if recurrences_conflict(
                    self.recurrence,
                    conflict.recurrence,
                    self.start,
                    conflict.start_time,
                    self.interval,
                    conflict.interval
                ):
                    errors.append((None, "This routine's recurrence and time overlaps with another existing recurring routine."))
                    break

        return errors
