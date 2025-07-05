from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from SOLIDIFY.categories.forms import CreateCategoryForm
from SOLIDIFY.categories.models import Category


# Create your views here.
class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class ListCategoriesView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'


    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)