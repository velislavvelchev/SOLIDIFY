from django.db import models


class ScheduledRoutine(models.Model):
    class Meta:
        verbose_name_plural = "Scheduled Routines"

    class RecurrenceChoices(models.TextChoices):
        NONE = 'none', 'None'
        DAILY = 'daily', 'Daily'
        WEEKLY = 'weekly', 'Weekly'
        MONTHLY = 'monthly', 'Monthly'

    routine = models.ForeignKey(
        to='routines.Routine',
        on_delete=models.CASCADE,
        related_name='scheduled_habits',
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    recurrence = models.CharField(
        max_length=10,
        choices=RecurrenceChoices.choices,
        default=RecurrenceChoices.NONE
    )

    interval = models.PositiveIntegerField(default=1)


