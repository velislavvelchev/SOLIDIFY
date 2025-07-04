from django.db import models


class ScheduledRoutine(models.Model):
    class Meta:
        verbose_name_plural = "Scheduled Routines"

    routine = models.ForeignKey(
        to='routines.Routine',
        on_delete=models.CASCADE,
        related_name='scheduled_habits',
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()


