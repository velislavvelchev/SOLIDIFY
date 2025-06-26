from django.db import models

# Create your models here.
class Category(models.Model):
	class CategoryChoices(models.TextChoices):
		DEFAULT = '', ''
		PHYSICAL = 'Physical', 'Physical'
		MENTAL = 'Mental', 'Mental'
		CREATIVE = 'Creative', 'Creative'
		FINANCIAL = 'Financial', 'Financial'

	category_type = models.CharField(
		default=CategoryChoices.DEFAULT,
		max_length=35,
		choices=CategoryChoices.choices
	)

	def __str__(self):
		return self.category_type