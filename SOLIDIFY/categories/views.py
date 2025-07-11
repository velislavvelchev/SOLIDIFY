from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from SOLIDIFY.categories.forms import CreateCategoryForm, EditCategoryForm
from SOLIDIFY.categories.models import Category


# Create your views here.
class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'categories/category_create.html'
    success_url = reverse_lazy('all-categories')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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



class EditCategoryView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Category
    form_class = EditCategoryForm
    template_name = 'categories/category_edit.html'
    success_url = reverse_lazy('all-categories')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk


class DetailsCategoryView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Category
    template_name = 'categories/category_details.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk


class DeleteCategoryView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('all-categories')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)