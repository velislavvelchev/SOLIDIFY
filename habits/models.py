from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class Habit(models.Model):
	category = models.ForeignKey(
        to = 'categories.Category',
        on_delete = models.CASCADE,
        related_name = 'category_habits'
	)

	is_completed = models.BooleanField(
		default=False,
	)

	priority = models.IntegerField(
		default=1,
		validators = [
			MaxValueValidator(5),
		]
	) # values from 1 to 5, put validator

	notes = models.TextField(
		null=True, blank=True
	)