from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    class CategoryChoices(models.TextChoices):
        DEFAULT = '', 'Select a category type'
        PHYSICAL = 'Physical', 'Physical'
        MENTAL = 'Mental', 'Mental'
        CREATIVE = 'Creative', 'Creative'
        FINANCIAL = 'Financial', 'Financial'

    category_type = models.CharField(
        max_length=35,
        choices=CategoryChoices.choices,
        default=CategoryChoices.DEFAULT,
        unique=True
    )

    description = models.TextField(
        max_length=50,
        blank=True,
        null=True,
    )

    min_habits_per_day = models.IntegerField(
        default=1,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.category_type