from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from SOLIDIFY.routines.validators import RoutineNameValidator

UserModel = get_user_model()


class Routine(models.Model):
    class Meta:
        verbose_name_plural = "Routines"
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'routine_name'],
                name='unique_routine_per_user'
            )
        ]

    routine_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(3, message="The routine name must be at least 3 characters long."),
            RoutineNameValidator(),
        ],
    )

    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.CASCADE,
        related_name='category_routines',
    )

    habits = models.ManyToManyField(
        'habits.Habit',
        blank=True,
        related_name='habits_routines',
    )


    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.routine_name

