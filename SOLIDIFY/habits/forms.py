from django import forms
from SOLIDIFY.habits.models import Habit


from django import forms
from .models import Habit

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
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select an existing category"


class CreateHabitForm(HabitBaseForm):
    pass