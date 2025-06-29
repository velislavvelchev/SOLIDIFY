from django import forms

from SOLIDIFY.schedule.models import ScheduledHabit


class ScheduleHabitBaseForm(forms.ModelForm):
    class Meta:
        model = ScheduledHabit
        fields = '__all__'


class ScheduleHabitCreateForm(ScheduleHabitBaseForm):
    pass
