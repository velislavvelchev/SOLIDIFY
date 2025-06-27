from django.db import models


class ScheduledHabit(models.Model):
    class Meta:
        unique_together = ('routine', 'habit', 'scheduled_time')

    routine = models.ForeignKey(
        to='routines.Routine',
        on_delete=models.CASCADE,
        related_name='scheduled_habits',
    )

    habit = models.ForeignKey(
        to='habits.Habit',
        on_delete=models.CASCADE,
    )

    scheduled_time = models.DateTimeField()

