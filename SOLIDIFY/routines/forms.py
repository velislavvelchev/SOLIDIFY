from django import forms
from .models import Routine

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
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select an existing category"




class CreateRoutineForm(RoutineBaseForm):
    pass

class EditRoutineForm(RoutineBaseForm):
    pass