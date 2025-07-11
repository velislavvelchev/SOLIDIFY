from django.urls import path, include
from .views import CalendarEventView, CalendarPageView, CreateScheduleRoutineView, CalendarEventUpdateView, \
    DeleteScheduleRoutineView

urlpatterns = [
    path('api/', include([
        path('events/', CalendarEventView.as_view(), name='calendar-events'),
        path('update/', CalendarEventUpdateView.as_view(), name='calendar-update')
    ])),
    path('', CalendarPageView.as_view(), name='calendar'),
    path('create/', CreateScheduleRoutineView.as_view(), name='schedule-create'),
    path('<int:pk>/', include([
        path('delete/', DeleteScheduleRoutineView.as_view(), name='schedule-delete')
    ]))
]
