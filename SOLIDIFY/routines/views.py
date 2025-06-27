from django.contrib.auth.mixins import LoginRequiredMixin
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
        return super().form_valid(form)

