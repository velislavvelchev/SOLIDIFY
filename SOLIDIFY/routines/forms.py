from django import forms
from .models import Routine
from ..categories.models import Category
from ..habits.models import Habit
from ..mixins import CoreModelFormMixin


class RoutineBaseForm(CoreModelFormMixin, forms.ModelForm):
    unique_field_name = 'routine_name'
    unique_error_msg = 'You already have a routine with this name.'
    user_queryset_fields = ['category']
    empty_labels = {'category': 'Select an existing category'}

    class Meta:
        model = Routine
        exclude = ('user',)
        widgets = {
            "routine_name": forms.TextInput(attrs={
                'placeholder': 'Name your routine (e.g. Morning Routine)'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.is_bound:  # only set queryset to none on GET, not POST
            self.fields['habits'].queryset = Habit.objects.none()



class CreateRoutineForm(RoutineBaseForm):
    pass

class EditRoutineForm(RoutineBaseForm):
    pass