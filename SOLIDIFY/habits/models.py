from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Habit(models.Model):
	class Meta:
		verbose_name_plural = "Habits"

	class HabitChoices(models.TextChoices):
		DEFAULT = '', 'Select dopamine type'
		ANTICIPATORY = 'Anticipatory', 'Anticipatory'
		REWARD = 'Reward', 'Reward'
		BOTH = 'Both', 'Both'

	dopamine_type = models.CharField(
		max_length=35, choices=HabitChoices.choices,
		default=HabitChoices.DEFAULT
	)

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
		max_length=50,
		null=True,
		blank=True
	)

	user = models.ForeignKey(
		to=UserModel,
		on_delete = models.CASCADE,
	)

	def __str__(self):
		return self.habit_name