from django.db import models


class Category(models.Model):
    class CategoryChoices(models.TextChoices):
        DEFAULT = '', ''
        PHYSICAL = 'Physical', 'Physical'
        MENTAL = 'Mental', 'Mental'
        CREATIVE = 'Creative', 'Creative'
        FINANCIAL = 'Financial', 'Financial'

    category_type = models.CharField(
        max_length=35,
        choices=CategoryChoices.choices,
        default=CategoryChoices.DEFAULT,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    min_habits_per_day = models.IntegerField(
        default=1,
    )

    def __str__(self):
        return self.category_type