from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CreateHabitForm


from django.http import JsonResponse
from .models import Habit


# Create your views here.
class CreateHabitView(LoginRequiredMixin, CreateView):
    model = Habit
    form_class = CreateHabitForm
    template_name = 'habits/create_habit.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)



class HabitsForCategoryView(ListView):
    model = Habit

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        habits = Habit.objects.filter(category_id=category_id)
        data = [
            {'id': h.id, 'name': h.habit_name}
            for h in habits
        ]
        return JsonResponse({'habits': data})


class ListHabitView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = 'habits/habits_list.html'
    context_object_name = 'habits'


    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)