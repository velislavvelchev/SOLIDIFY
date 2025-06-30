from django import forms

from SOLIDIFY.schedule.models import ScheduledRoutine


class ScheduleRoutineBaseForm(forms.ModelForm):
    class Meta:
        model = ScheduledRoutine
        fields = '__all__'


class ScheduleRoutineCreateForm(ScheduleRoutineBaseForm):
    pass
