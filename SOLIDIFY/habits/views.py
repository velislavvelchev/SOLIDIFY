from django.urls import reverse_lazy
from django.views.generic import CreateView
from SOLIDIFY.habits.forms import CreateHabitForm
from SOLIDIFY.habits.models import Habit


# Create your views here.
class CreateHabitView(CreateView):
    model = Habit
    form_class = CreateHabitForm
    template_name = 'habits/create_habit.html'
    success_url = reverse_lazy('home')