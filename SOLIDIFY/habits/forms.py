from django import forms
from SOLIDIFY.habits.models import Habit


class HabitBaseForm(forms.ModelForm):
    class Meta:
        model = Habit
        exclude = ('user', )


class CreateHabitForm(HabitBaseForm):
    pass