from django import forms
from SOLIDIFY.habits.models import Habit

from django import forms
from .models import Habit
from ..categories.models import Category
from ..mixins import CoreModelFormMixin


class HabitBaseForm(CoreModelFormMixin, forms.ModelForm):
    unique_field_name = 'habit_name'
    unique_error_msg = 'You already have a habit with this name.'
    user_queryset_fields = ['category']
    empty_labels = {'category': 'Select an existing category'}


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


class CreateHabitForm(HabitBaseForm):
    pass

class EditHabitForm(HabitBaseForm):
    pass