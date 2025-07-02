import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views import View

from .forms import ScheduleRoutineCreateForm
from .models import ScheduledRoutine
from django.views.generic import TemplateView, CreateView


# Create your views here.

# for test purpose at this point
class CalendarEventView(View):
    def get(self, request):
        user = request.user
        scheduled_routines = ScheduledRoutine.objects.filter(routine__user=user)

        events = [
            {
                "title": s.routine.routine_name,
                "start": s.scheduled_time.isoformat(),
                "id": s.id,
                                            }
            for s in scheduled_routines
        ]
        return JsonResponse(events, safe=False)




class CalendarPageView(LoginRequiredMixin, TemplateView):
    template_name = 'schedule/calendar.html'



class ScheduleRoutineCreateView(LoginRequiredMixin, CreateView):
    model = ScheduledRoutine
    form_class = ScheduleRoutineCreateForm
    template_name = 'schedule/create_schedule.html'
    success_url = reverse_lazy('calendar')


    def form_valid(self, form):
        scheduled = form.save(commit=False)

        # Get the hidden UTC field from POST
        utc_string = self.request.POST.get('scheduled_time_utc')
        dt_utc = parse_datetime(utc_string) if utc_string else None

        # If we have a value, use it
        # ... inside your view
        if dt_utc is not None:
            dt_utc = timezone.make_aware(dt_utc, datetime.timezone.utc)
            scheduled.scheduled_time = dt_utc

        # Validate time is not in the past
        if scheduled.scheduled_time < timezone.now():
            form.add_error('scheduled_time', "You cannot schedule a habit in the past.")
            return self.form_invalid(form)


        return super().form_valid(form)


