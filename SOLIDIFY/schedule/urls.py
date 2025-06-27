from django.urls import path
from .views import CalendarEventView, CalendarPageView

urlpatterns = [
    path('events/', CalendarEventView.as_view(), name='calendar_events'),
    path('', CalendarPageView.as_view(), name='calendar'),

]
