from django.db import models


class ScheduledRoutine(models.Model):

    routine = models.ForeignKey(
        to='routines.Routine',
        on_delete=models.CASCADE,
        related_name='scheduled_habits',
    )

    start_time = models.DateTimeField(
        null=True,
        blank=True
    )

    end_time = models.DateTimeField(
        null=True,
        blank=True
    )


