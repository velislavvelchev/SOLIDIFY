from django import forms

from SOLIDIFY.routines.models import Routine


class RoutineBaseForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'


class CreateRoutineForm(RoutineBaseForm):
    pass