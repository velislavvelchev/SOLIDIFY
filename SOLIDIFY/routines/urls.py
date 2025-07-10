from django.urls import path, include

from SOLIDIFY.routines.views import CreateRoutineView, ListRoutinesView, EditRoutineView, DetailsRoutineView, \
    DeleteRoutineView

urlpatterns = [
    path('create/', CreateRoutineView.as_view(), name='create-routine'),
    path('all-routines/', ListRoutinesView.as_view(), name='all-routines'),
    path('<int:pk>/', include([
        path('edit/', EditRoutineView.as_view(), name='edit-routine'),
        path('details/',  DetailsRoutineView.as_view(), name='details-routine'),
        path('delete/', DeleteRoutineView.as_view(), name='delete-routine'),
    ]))
]