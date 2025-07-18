from rest_framework import serializers
from SOLIDIFY.habits.models import Habit


class HabitSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'habit_name')