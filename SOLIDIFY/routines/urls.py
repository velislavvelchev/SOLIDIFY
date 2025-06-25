from django.urls import path

from SOLIDIFY.routines.views import CreateRoutineView

urlpatterns = [
    path('create/', CreateRoutineView.as_view(), name='create-routine')
]