from django import forms

from SOLIDIFY.categories.models import Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CreateCategoryForm(CategoryBaseForm):
    pass
