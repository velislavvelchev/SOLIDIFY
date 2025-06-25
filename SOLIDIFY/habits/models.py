from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class Habit(models.Model):
	habit_name = models.CharField(
		max_length=30,
	)

	category = models.ForeignKey(
        to = 'categories.Category',
        on_delete = models.CASCADE,
        related_name = 'category_habits'
	)

	is_completed = models.BooleanField(
		default=False,
	)

	created_at = models.DateTimeField(
		auto_now_add = True,
	)

	priority = models.IntegerField(
		default=1,
		validators = [
			MaxValueValidator(5),
		]
	)

	notes = models.TextField(
		null=True, blank=True
	)

	def __str__(self):
		return self.habit_name