from django.http import JsonResponse
from django.views import View
from .models import ScheduledHabit
from django.views.generic import TemplateView
# Create your views here.


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
