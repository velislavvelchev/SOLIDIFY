import datetime
import json

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import ScheduleRoutineCreateForm
from .models import ScheduledRoutine
from django.views.generic import TemplateView, CreateView

from ..routines.models import Routine


# Create your views here.

# for test purpose at this point
class CalendarEventView(View):
    def get(self, request):
        user = request.user
        scheduled_routines = ScheduledRoutine.objects.filter(routine__user=user)
        events = [
            {
                "title": s.routine.routine_name,
                "start": s.start_time.isoformat() if s.start_time else None,
                "end": s.end_time.isoformat() if s.end_time else None,
                "id": s.id,
            }
            for s in scheduled_routines
        ]
        return JsonResponse(events, safe=False)



@method_decorator(csrf_exempt, name='dispatch')  # Optional if you add CSRF in JS
class CalendarEventUpdateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            event_id = data.get("id")
            start = data.get("start")
            end = data.get("end")

            if not event_id or not start:
                return JsonResponse({"success": False, "error": "Missing required fields."})

            scheduled = ScheduledRoutine.objects.filter(
                id=event_id,
                routine__user=request.user
            ).first()
            if not scheduled:
                return JsonResponse({"success": False, "error": "Event not found or no permission."})

            scheduled.start_time = parse_datetime(start)
            scheduled.end_time = parse_datetime(end) if end else None
            scheduled.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})


class CalendarPageView(LoginRequiredMixin, TemplateView):
    template_name = 'schedule/calendar.html'


class ScheduleRoutineCreateView(LoginRequiredMixin, CreateView):
    model = ScheduledRoutine
    form_class = ScheduleRoutineCreateForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('calendar')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Limit routines to those belonging to the current user
        form.fields['routine'].queryset = Routine.objects.filter(user=self.request.user)
        return form


    def form_valid(self, form):
        scheduled = form.save(commit=False)

        # Grab the hidden UTC fields from POST data
        start_utc_str = self.request.POST.get('start_time_utc')
        end_utc_str = self.request.POST.get('end_time_utc')

        start_dt_utc = parse_datetime(start_utc_str)
        end_dt_utc = parse_datetime(end_utc_str)

        # Assign to model fields, making sure they're timezone aware
        if start_dt_utc is not None:
            start_dt_utc = timezone.make_aware(start_dt_utc, datetime.timezone.utc)
            scheduled.start_time = start_dt_utc


        if end_dt_utc is not None:
            end_dt_utc = timezone.make_aware(end_dt_utc, datetime.timezone.utc)
            scheduled.end_time = end_dt_utc

        # Validate: start < end
        if scheduled.start_time and scheduled.end_time:
            if scheduled.start_time >= scheduled.end_time:
                form.add_error('start_time', "Start time must be before end time.")
                form.add_error('end_time', "End time must be after start time.")
                return self.form_invalid(form)

        # Validate: can't schedule in the past
        now = timezone.now()
        if scheduled.start_time and scheduled.start_time < now:
            form.add_error('start_time', "You cannot schedule a routine in the past.")
            return self.form_invalid(form)

        # Validate: no overlap with existing routines for this user
        if scheduled.routine and scheduled.start_time and scheduled.end_time:
            user = scheduled.routine.user
            conflicts = ScheduledRoutine.objects.filter(
                routine__user=user,
                start_time__lt=scheduled.end_time,
                end_time__gt=scheduled.start_time,
            )
            # If editing, exclude self: .exclude(pk=scheduled.pk)
            if conflicts.exists():
                form.add_error(None, "This routine overlaps with another scheduled routine.")
                return self.form_invalid(form)

        return super().form_valid(form)



