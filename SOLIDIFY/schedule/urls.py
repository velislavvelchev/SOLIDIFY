from django.urls import path, include
from .views import CalendarEventAPIView, CalendarPageView, CreateScheduleRoutineView, CalendarEventUpdateAPIView, \
    DeleteScheduleRoutineView

urlpatterns = [
    path('api/', include([
        path('events/', CalendarEventAPIView.as_view(), name='calendar-events'),
        path('update/<int:pk>/', CalendarEventUpdateAPIView.as_view(), name='calendar-update')
    ])),
    path('calendar/', CalendarPageView.as_view(), name='calendar'),
    path('create/', CreateScheduleRoutineView.as_view(), name='schedule-create'),
    path('<int:pk>/', include([
        path('delete/', DeleteScheduleRoutineView.as_view(), name='schedule-delete')
    ]))
]
