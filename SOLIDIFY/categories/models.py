from django.db import models

# Create your models here.
class Category(models.Model):
	class CategoryChoices(models.TextChoices):
		PHYSICAL = 'Physical', 'Physical'
		MENTAL = 'Mental', 'Mental'
		CREATIVE = 'Creative', 'Creative'
		FINANCIAL = 'Financial', 'Financial'

	category_type = models.CharField(
		max_length=35, choices=CategoryChoices.choices
	)

	