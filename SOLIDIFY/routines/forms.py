from django import forms

from SOLIDIFY.routines.models import Routine


class RoutineBaseForm(forms.ModelForm):
    class Meta:
        model = Routine
        exclude = ('user', )


class CreateRoutineForm(RoutineBaseForm):
    pass