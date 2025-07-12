import datetime

from django import forms

from django.utils import timezone
from django.utils.dateparse import parse_datetime

from SOLIDIFY.schedule.models import ScheduledRoutine


class ScheduleRoutineBaseForm(forms.ModelForm):
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

        return cleaned_data




class ScheduleRoutineCreateForm(ScheduleRoutineBaseForm):
    pass
