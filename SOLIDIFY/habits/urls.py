from django.urls import path, include
from SOLIDIFY.habits.views import CreateHabitView, HabitsForCategoryView, ListHabitView, EditHabitView, DetailsHabitView

urlpatterns = [
    path('create/', CreateHabitView.as_view(), name='create-habit'),
    path('api/habits-for-category/', HabitsForCategoryView.as_view(), name='habits-for-category'),
    path('all-habits/', ListHabitView.as_view(), name='all-habits'),
    path('<int:pk>/', include([
        path('edit/', EditHabitView.as_view(), name='edit-habit'),
        path('details/', DetailsHabitView.as_view(), name='details-habit'),
    ]))
]
