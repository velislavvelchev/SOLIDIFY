from django.urls import path
from SOLIDIFY.habits.views import CreateHabitView, HabitsForCategoryView, ListHabitView

urlpatterns = [
    path('create/', CreateHabitView.as_view(), name='create-habit'),
    path('api/habits-for-category/', HabitsForCategoryView.as_view(), name='habits-for-category'),
    path('all-habits/', ListHabitView.as_view(), name='all-habits'),
]