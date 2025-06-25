from django import forms
from SOLIDIFY.habits.models import Habit


class HabitBaseForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = '__all__'


class CreateHabitForm(HabitBaseForm):
    pass