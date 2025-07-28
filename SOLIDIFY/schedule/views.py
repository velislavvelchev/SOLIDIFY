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




class DeleteScheduleRoutineView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ScheduledRoutine
    success_url = reverse_lazy('calendar')

    def test_func(self):
        obj = self.get_object()
        return obj.routine.user == self.request.user

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.success_url)


