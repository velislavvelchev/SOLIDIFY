import datetime
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY

from django import forms

from django.utils import timezone
from django.utils.dateparse import parse_datetime

from SOLIDIFY.schedule.models import ScheduledRoutine


class ScheduleRoutineBaseForm(forms.ModelForm):
    FREQ_MAP = {
        'daily': DAILY,
        'weekly': WEEKLY,
        'monthly': MONTHLY
    }

    MAX_LOOKAHEAD_DAYS = 60  # how far ahead to simulate recurrence

    RECURRENCE_CHOICES = [
        ('none', 'Do not repeat'),
        ('daily', 'Repeat daily'),
        ('weekly', 'Repeat weekly'),
        ('monthly', 'Repeat monthly'),
    ]

    recurrence = forms.ChoiceField(
        choices=RECURRENCE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    start_time_utc = forms.CharField(
        widget=forms.HiddenInput(attrs={'id': 'start_time_utc'}),
        required=False
    )
    end_time_utc = forms.CharField(
        widget=forms.HiddenInput(attrs={'id': 'end_time_utc'}),
        required=False
    )

    class Meta:
        model = ScheduledRoutine
        fields = '__all__'
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'id': 'start_time'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'id': 'end_time'}),
        }


    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['routine'].empty_label = "Select an existing routine"



    def clean(self):
        cleaned_data = super().clean()
        start_utc_str = cleaned_data.get('start_time_utc')
        end_utc_str = cleaned_data.get('end_time_utc')
        routine = cleaned_data.get('routine')


        start_time = parse_datetime(start_utc_str)
        if start_time is not None:
            start_time = timezone.make_aware(start_time, datetime.timezone.utc)
            cleaned_data['start_time'] = start_time



        end_time = parse_datetime(end_utc_str)
        if end_time is not None:
            end_time = timezone.make_aware(end_time, datetime.timezone.utc)
            cleaned_data['end_time'] = end_time


        # Validate: start < end
        if start_time and end_time:
            if start_time >= end_time:
                self.add_error('start_time', "Start time must be before end time.")
                self.add_error('end_time', "End time must be after start time.")

        # Validate: can't schedule in the past
        now = timezone.now()
        if start_time and start_time < now:
            self.add_error('start_time', "You cannot schedule a routine in the past.")

        # Validate: no overlap with existing routines for this user
        # (Assuming self._user is set in __init__)
        if routine and start_time and end_time and hasattr(self, '_user') and self._user:
            conflicts = ScheduledRoutine.objects.filter(
                routine__user=self._user,
                start_time__lt=end_time,
                end_time__gt=start_time,
            )
            # Exclude self when editing
            if self.instance.pk:
                conflicts = conflicts.exclude(pk=self.instance.pk)
            if conflicts.exists():
                self.add_error(None, "This routine overlaps with another scheduled routine.")

        if routine and start_time and end_time and hasattr(self, '_user') and self._user:
            recurrence_conflicts = []

            for existing in ScheduledRoutine.objects.filter(routine__user=self._user):
                if existing.pk == self.instance.pk:
                    continue  # Skip self

                if existing.recurrence != 'none':
                    freq = self.FREQ_MAP.get(existing.recurrence)
                    if freq:
                        # Build recurrence rule for next N days
                        rule = rrule(
                            freq,
                            dtstart=existing.start_time,
                            until=start_time + datetime.timedelta(days=self.MAX_LOOKAHEAD_DAYS)
                        )
                        for occ_start in rule:
                            occ_end = occ_start + (existing.end_time - existing.start_time)
                            if start_time < occ_end and end_time > occ_start:
                                recurrence_conflicts.append((occ_start, occ_end))
                                break  # One conflict is enough
                else:
                    # Single instance overlap (already handled but duplicated here for completeness)
                    if start_time < existing.end_time and end_time > existing.start_time:
                        recurrence_conflicts.append((existing.start_time, existing.end_time))

            if recurrence_conflicts:
                self.add_error(None, "This routine conflicts with a recurring routine already scheduled.")

        return cleaned_data




class ScheduleRoutineCreateForm(ScheduleRoutineBaseForm):
    pass
