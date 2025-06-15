from django.db import models

# Create your models here.
class Routine(models.Model):
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