from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .forms import CreateHabitForm, EditHabitForm

from django.http import JsonResponse, HttpResponseRedirect
from .models import Habit
from .serializers import HabitSimpleSerializer
from ..categories.models import Category


# Create your views here.
class CreateHabitView(LoginRequiredMixin, CreateView):
    model = Habit
    form_class = CreateHabitForm
    template_name = 'habits/habit_create.html'
    success_url = reverse_lazy('all-habits')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)



class HabitsForCategoryAPIView(ListAPIView):
    serializer_class = HabitSimpleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        category_id = self.request.GET.get('category_id')
        return Habit.objects.filter(category_id=category_id, user=user)


class ListHabitView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = 'habits/habits_list.html'
    context_object_name = 'habits'


    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)



class EditHabitView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Habit
    form_class = EditHabitForm
    template_name = 'habits/habit_edit.html'
    success_url = reverse_lazy('all-habits')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk



class DetailsHabitView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Habit
    template_name = 'habits/habit_details.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk


class DeleteHabitView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Habit
    success_url = reverse_lazy('all-habits')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)