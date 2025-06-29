from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View

from .forms import ScheduleHabitCreateForm
from .models import ScheduledHabit
from django.views.generic import TemplateView, CreateView


# Create your views here.

# for test purpose at this point
class CalendarEventView(View):
    def get(self, request):
        user = request.user
        habits = ScheduledHabit.objects.filter(routine__user=user)

        events = [
            {
                "title": f"{h.habit.habit_name}",
                "start": h.scheduled_time.isoformat(),
                "id": h.id,
                "routine": h.routine.routine_name,
            }
            for h in habits
        ]

        return JsonResponse(events, safe=False)



class CalendarPageView(TemplateView):
    template_name = 'schedule/calendar.html'


class ScheduleHabitCreateView(CreateView):
    model = ScheduledHabit
    form_class = ScheduleHabitCreateForm
    template_name = 'schedule/create_schedule_habit.html'
    success_url = reverse_lazy('calendar')

    def form_valid(self, form):
        scheduled = form.save(commit=False)

        # Validate time is not in the past
        if scheduled.scheduled_time < timezone.now():
            form.add_error('scheduled_time', "You cannot schedule a habit in the past.")
            return self.form_invalid(form)

        # Validate time within routine window
        if not (scheduled.routine.start_date <= scheduled.scheduled_time.date() <= scheduled.routine.end_date):
            form.add_error('scheduled_time', "Time must be within routine start and end date.")
            return self.form_invalid(form)

        return super().form_valid(form)


