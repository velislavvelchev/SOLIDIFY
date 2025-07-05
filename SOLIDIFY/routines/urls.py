from django.urls import path

from SOLIDIFY.routines.views import CreateRoutineView, ListRoutinesView

urlpatterns = [
    path('create/', CreateRoutineView.as_view(), name='create-routine'),
    path('all-routines/', ListRoutinesView.as_view(), name='all-routines'),
]