from django.urls import path

from SOLIDIFY.habits.views import CreateHabitView

urlpatterns = [
    path('create/', CreateHabitView.as_view(), name='create-habit')
]