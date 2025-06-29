from django.urls import path
from .views import CalendarEventView, CalendarPageView, ScheduleHabitCreateView

urlpatterns = [
    path('events/', CalendarEventView.as_view(), name='calendar-events'),
    path('', CalendarPageView.as_view(), name='calendar'),
    path('create/', ScheduleHabitCreateView.as_view(), name='schedule-create'),

]
