from django import forms

from SOLIDIFY.schedule.models import ScheduledRoutine


class ScheduleRoutineBaseForm(forms.ModelForm):
    class Meta:
        model = ScheduledRoutine
        fields = '__all__'
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'id': 'scheduled_time'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['routine'].empty_label = "Select an existing routine"


class ScheduleRoutineCreateForm(ScheduleRoutineBaseForm):
    pass
