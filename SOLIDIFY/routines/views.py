from django.urls import reverse_lazy
from django.views.generic import CreateView

from SOLIDIFY.routines.forms import CreateRoutineForm
from SOLIDIFY.routines.models import Routine


# Create your views here.
class CreateRoutineView(CreateView):
    model = Routine
    form_class = CreateRoutineForm
    template_name = 'routines/create_routine.html'
    success_url = reverse_lazy('home')