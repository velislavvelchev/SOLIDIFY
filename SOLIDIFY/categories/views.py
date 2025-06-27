from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from SOLIDIFY.categories.forms import CreateCategoryForm
from SOLIDIFY.categories.models import Category


# Create your views here.
class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('home')

