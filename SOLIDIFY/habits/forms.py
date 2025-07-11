from django import forms
from SOLIDIFY.habits.models import Habit


from django import forms
from .models import Habit
from ..categories.models import Category


class HabitBaseForm(forms.ModelForm):
    class Meta:
        model = Habit
        exclude = ('user', 'is_completed',)
        widgets = {
            'dopamine_type': forms.Select(attrs={
            }),
            'habit_name': forms.TextInput(attrs={
                'placeholder': 'Name your habit (e.g. Drink water)'
            }),
            'category': forms.Select(),
            'priority': forms.TextInput(attrs={
                'placeholder': 'Priority (1=low, 5=high)',
                'pattern': '[1-5]',
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Add any notes or details (optional)',
                'rows': 2,
            }),
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)  # get the user passed from the view
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select an existing category"
        if self._user is not None:
            self.fields['category'].queryset = Category.objects.filter(user=self._user)


    def clean(self):
        cleaned_data = super().clean()
        user = self._user
        habit_name = cleaned_data.get('habit_name')

        if user and habit_name:
            qs = Habit.objects.filter(user=user, habit_name=habit_name)
            # Exclude current instance on update
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error('habit_name', 'You already have a habit with this name.')
        return cleaned_data




class CreateHabitForm(HabitBaseForm):
    pass

class EditHabitForm(HabitBaseForm):
    pass