from django.urls import path
from .views import CalendarEventView, CalendarPageView, ScheduleRoutineCreateView

urlpatterns = [
    path('api/events/', CalendarEventView.as_view(), name='calendar-events'),
    path('', CalendarPageView.as_view(), name='calendar'),
    path('create/', ScheduleRoutineCreateView.as_view(), name='schedule-create'),

]
