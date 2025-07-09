from django.urls import path, include
from .views import CalendarEventView, CalendarPageView, ScheduleRoutineCreateView, CalendarEventUpdateView, \
    ScheduleRoutineDeleteView

urlpatterns = [
    path('api/', include([
        path('events/', CalendarEventView.as_view(), name='calendar-events'),
        path('update/', CalendarEventUpdateView.as_view(), name='calendar-update')
    ])),
    path('', CalendarPageView.as_view(), name='calendar'),
    path('create/', ScheduleRoutineCreateView.as_view(), name='schedule-create'),
    path('<int:pk>/', include([
        path('delete/', ScheduleRoutineDeleteView.as_view(), name='calendar-delete')
    ]))
]
