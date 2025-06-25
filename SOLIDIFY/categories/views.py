from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from SOLIDIFY.categories.forms import CreateCategoryForm
from SOLIDIFY.categories.models import Category


# Create your views here.
class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('home')

