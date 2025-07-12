from django import forms

from SOLIDIFY.categories.models import Category
from django import forms
from .models import Category
from ..mixins import CoreModelFormMixin


class CategoryBaseForm(CoreModelFormMixin, forms.ModelForm):
    unique_field_name = 'category_type'
    unique_error_msg = 'You already have a category with this type.'
    user_queryset_fields = ['category_type']
    empty_labels = {'category_type': 'Select an existing category'}

    class Meta:
        model = Category
        exclude = ('user', )
        widgets = {
            'category_type': forms.Select(attrs={
                'placeholder': 'Select category type',  # Note: placeholder has no effect on <select>, but label/empty_label can help
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe this category (optional)',
                'rows': 2,
            }),
            'min_habits_per_day': forms.TextInput(attrs={
                'placeholder': 'Minimum habits per day (e.g. 1)',
            }),
        }




class CreateCategoryForm(CategoryBaseForm):
    pass

class EditCategoryForm(CategoryBaseForm):
    class Meta(CategoryBaseForm.Meta):
        exclude = ('user', 'min_habits_per_day')
