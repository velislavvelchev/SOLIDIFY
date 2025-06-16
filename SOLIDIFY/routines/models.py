from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Routine(models.Model):
	routine_name = models.CharField(
		unique=True,
		max_length=30,
		validators=[
			MinLengthValidator(3, message="The routine name must be at least 3 characters long."),
			#TODO custom validator that checks for characters only
		]
	)
	category = models.ForeignKey(
		to ='categories.Category',
		on_delete = models.CASCADE,
		related_name = 'category_routines'
	)

	recommended_habits = models.ManyToManyField(
		'habits.Habit',
		blank=True,
		related_name='recommended_in_routines'
    )