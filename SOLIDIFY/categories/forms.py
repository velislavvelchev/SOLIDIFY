from django import forms

from SOLIDIFY.categories.models import Category


from django import forms
from .models import Category

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
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
