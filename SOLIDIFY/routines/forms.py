from django import forms
from .models import Routine
from ..categories.models import Category
from ..habits.models import Habit


class RoutineBaseForm(forms.ModelForm):
    class Meta:
        model = Routine
        exclude = ('user',)
        widgets = {
            "routine_name": forms.TextInput(attrs={
                'placeholder': 'Name your routine (e.g. Morning Routine)'
            }),
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)  # get the user passed from the view
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select an existing category"
        if self._user is not None:
            self.fields['category'].queryset = Category.objects.filter(user=self._user)

        self.fields['habits'].queryset = Habit.objects.none()


    def clean(self):
        cleaned_data = super().clean()
        user = self._user
        routine_name = cleaned_data.get('routine_name')

        if user and routine_name:
            qs = Routine.objects.filter(user=user, routine_name=routine_name)
            # Exclude current instance on update
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error('routine_name', 'You already have a routine with this name.')
        return cleaned_data


class CreateRoutineForm(RoutineBaseForm):
    pass

class EditRoutineForm(RoutineBaseForm):
    pass