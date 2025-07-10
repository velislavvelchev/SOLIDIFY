from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from SOLIDIFY.routines.forms import CreateRoutineForm, EditRoutineForm
from SOLIDIFY.routines.models import Routine


# Create your views here.
class CreateRoutineView(LoginRequiredMixin, CreateView):
    model = Routine
    form_class = CreateRoutineForm
    template_name = 'routines/routine_create.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        routine = form.save(commit=False)
        habits = form.cleaned_data['habits']
        category = routine.category

        matching_habits = [h for h in habits if h.category == category]
        required = category.min_habits_per_day

        if len(matching_habits) < required:
            form.add_error('habits', f"Select at least {required} habit(s) from the '{category}' category.")
            return self.form_invalid(form)

        return super().form_valid(form)


class ListRoutinesView(LoginRequiredMixin, ListView):
    model = Routine
    template_name = 'routines/routine_list.html'
    context_object_name = 'routines'


    def get_queryset(self):
        return Routine.objects.filter(user=self.request.user)


class EditRoutineView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Routine
    form_class = EditRoutineForm
    template_name = 'routines/routine_edit.html'
    success_url = reverse_lazy('all-routines')

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk

class DetailsRoutineView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Routine
    template_name = 'routines/routine_details.html'

    def test_func(self):
        return self.request.user.pk == self.get_object().user.pk


class DeleteRoutineView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Routine
    success_url = reverse_lazy('all-routines')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)