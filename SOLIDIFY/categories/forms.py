from django import forms

from SOLIDIFY.categories.models import Category


from django import forms
from .models import Category

class CategoryBaseForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)  # get the user passed from the view
        super().__init__(*args, **kwargs)
        self.fields['category_type'].empty_label = "Select an existing category"
        if self._user is not None:
            self.fields['category_type'].queryset = Category.objects.filter(user=self._user)

    def clean(self):
        cleaned_data = super().clean()
        user = self._user
        category_type = cleaned_data.get('category_type')

        if user and category_type:
            qs = Category.objects.filter(user=user, category_type=category_type)
            # Exclude current instance on update
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                self.add_error('category_type', 'You already have a category with this type.')
        return cleaned_data


class CreateCategoryForm(CategoryBaseForm):
    pass

class EditCategoryForm(CategoryBaseForm):
    class Meta(CategoryBaseForm.Meta):
        exclude = ('user', 'min_habits_per_day')
