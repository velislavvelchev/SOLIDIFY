from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import CreateView
from SOLIDIFY.routines.forms import CreateRoutineForm
from SOLIDIFY.routines.models import Routine


# Create your views here.
class CreateRoutineView(LoginRequiredMixin, CreateView):
    model = Routine
    form_class = CreateRoutineForm
    template_name = 'routines/create_routine.html'
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


