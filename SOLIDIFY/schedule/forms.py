from django import forms

from SOLIDIFY.schedule.models import ScheduledRoutine


class ScheduleRoutineBaseForm(forms.ModelForm):
    class Meta:
        model = ScheduledRoutine
        fields = '__all__'
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'id': 'scheduled_time'})
        }
        

class ScheduleRoutineCreateForm(ScheduleRoutineBaseForm):
    pass
