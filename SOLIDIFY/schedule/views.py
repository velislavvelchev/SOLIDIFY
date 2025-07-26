from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .forms import ScheduleRoutineCreateForm
from .models import ScheduledRoutine
from django.views.generic import TemplateView, CreateView, DeleteView

from .serializers import ScheduledRoutineCalendarSerializer
from ..routines.models import Routine


# Create your views here.


class CalendarEventAPIView(ListAPIView):
    serializer_class = ScheduledRoutineCalendarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ScheduledRoutine.objects.filter(routine__user=self.request.user)

# @method_decorator(csrf_exempt, name='dispatch')  # Optional if you add CSRF in JS
# class CalendarEventUpdateView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             event_id = data.get("id")
#             start = data.get("start")
#             end = data.get("end")
#
#             if not event_id or not start:
#                 return JsonResponse({"success": False, "error": "Missing required fields."})
#
#             scheduled = ScheduledRoutine.objects.filter(
#                 id=event_id,
#                 routine__user=request.user
#             ).first()
#             if not scheduled:
#                 return JsonResponse({"success": False, "error": "Event not found or no permission."})
#
#             scheduled.start_time = parse_datetime(start)
#             scheduled.end_time = parse_datetime(end) if end else None
#             scheduled.save()
#
#             return JsonResponse({"success": True})
#         except Exception as e:
#             return JsonResponse({"success": False, "error": str(e)})

# class CalendarEventUpdateAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         event_id = request.data.get("id")
#         start = request.data.get("start")
#         end = request.data.get("end")
#
#         if not event_id or not start:
#             return Response({"success": False, "error": "Missing required fields."}, status=400)
#
#         scheduled = ScheduledRoutine.objects.filter(
#             id=event_id,
#             routine__user=request.user
#         ).first()
#         if not scheduled:
#             return Response({"success": False, "error": "Event not found or no permission."}, status=404)
#
#         # Validations: Don't allow scheduling in the past, etc.
#         start_dt = parse_datetime(start)
#         end_dt = parse_datetime(end) if end else None
#
#         # Example validation:
#         if start_dt and start_dt < timezone.now():
#             return Response({"success": False, "error": "Cannot schedule in the past."}, status=400)
#
#         scheduled.start_time = start_dt
#         scheduled.end_time = end_dt
#         scheduled.save()
#
#         return Response({"success": True})

class CalendarEventUpdateAPIView(UpdateAPIView):
    serializer_class = ScheduledRoutineCalendarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow users to update their own events
        return ScheduledRoutine.objects.filter(routine__user=self.request.user)

    # Override partial_update to customize response
    def partial_update(self, request, *args, **kwargs):
        # PATCH logic, called when PATCH is used
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True})
        else:
            # Get first error message, flatten if needed
            error_msg = serializer.errors
            if isinstance(error_msg, dict):
                # Return first error message string
                error_values = list(error_msg.values())
                error_list = error_values[0] if error_values else ["Invalid input"]
                error_str = error_list[0] if isinstance(error_list, list) else error_list
            else:
                error_str = "Invalid input"
            return Response({"success": False, "error": error_str}, status=400)

class CalendarPageView(LoginRequiredMixin, TemplateView):
    template_name = 'schedule/calendar.html'


class CreateScheduleRoutineView(LoginRequiredMixin, CreateView):
    model = ScheduledRoutine
    form_class = ScheduleRoutineCreateForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('calendar')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Limit routines to those belonging to the current user
        form.fields['routine'].queryset = Routine.objects.filter(user=self.request.user)
        return form


    # def form_valid(self, form):
    #     scheduled = form.save(commit=False)
    #
    #     # Grab the hidden UTC fields from POST data
    #     start_utc_str = self.request.POST.get('start_time_utc')
    #     end_utc_str = self.request.POST.get('end_time_utc')
    #
    #     start_dt_utc = parse_datetime(start_utc_str)
    #     end_dt_utc = parse_datetime(end_utc_str)
    #
    #     # Assign to model fields, making sure they're timezone aware
    #     if start_dt_utc is not None:
    #         start_dt_utc = timezone.make_aware(start_dt_utc, datetime.timezone.utc)
    #         scheduled.start_time = start_dt_utc
    #
    #
    #     if end_dt_utc is not None:
    #         end_dt_utc = timezone.make_aware(end_dt_utc, datetime.timezone.utc)
    #         scheduled.end_time = end_dt_utc
    #
    #     # Validate: start < end
    #     if scheduled.start_time and scheduled.end_time:
    #         if scheduled.start_time >= scheduled.end_time:
    #             form.add_error('start_time', "Start time must be before end time.")
    #             form.add_error('end_time', "End time must be after start time.")
    #             return self.form_invalid(form)
    #
    #     # Validate: can't schedule in the past
    #     now = timezone.now()
    #     if scheduled.start_time and scheduled.start_time < now:
    #         form.add_error('start_time', "You cannot schedule a routine in the past.")
    #         return self.form_invalid(form)
    #
    #     # Validate: no overlap with existing routines for this user
    #     if scheduled.routine and scheduled.start_time and scheduled.end_time:
    #         user = scheduled.routine.user
    #         conflicts = ScheduledRoutine.objects.filter(
    #             routine__user=user,
    #             start_time__lt=scheduled.end_time,
    #             end_time__gt=scheduled.start_time,
    #         )
    #         # If editing, exclude self: .exclude(pk=scheduled.pk)
    #         if conflicts.exists():
    #             form.add_error(None, "This routine overlaps with another scheduled routine.")
    #             return self.form_invalid(form)
    #
    #     return super().form_valid(form)



class DeleteScheduleRoutineView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ScheduledRoutine
    success_url = reverse_lazy('calendar')

    def test_func(self):
        obj = self.get_object()
        return obj.routine.user == self.request.user

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)


