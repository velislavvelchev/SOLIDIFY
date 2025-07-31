from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .forms import ScheduleRoutineCreateForm
from .models import ScheduledRoutine
from django.views.generic import TemplateView, CreateView, DeleteView

from .serializers import ScheduledRoutineCalendarSerializer
from ..accounts.permissions import ApiPermission
from ..routines.models import Routine


# Create your views here.


class CalendarEventAPIView(ListAPIView):
    serializer_class = ScheduledRoutineCalendarSerializer
    permission_classes = [ApiPermission]

    def get_queryset(self):
        return ScheduledRoutine.objects.filter(routine__user=self.request.user)


class CalendarEventUpdateAPIView(UpdateAPIView):
    serializer_class = ScheduledRoutineCalendarSerializer
    permission_classes = [ApiPermission]

    def get_queryset(self):
        return ScheduledRoutine.objects.filter(routine__user=self.request.user)

    # PATCH logic, called when PATCH is used (user drags the routine)
    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True})
        else:
            error = next(iter(serializer.errors.values()))[0]
            return Response({"success": False, "error": error}, status=400)


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


