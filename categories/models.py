from django.db import models

# Create your models here.
class Category(models.Model):
	class CategoryChoices(models.TextChoices):
		SPORTS = 'Sports', 'Sports'
		FAMILY_AND_FREE_TIME = 'Family and Free Time', 'Family and Free Time'
		PHYSICAL_AND_MENTAL_HEALTH = 'Physical and Mental Health', 'Physical and Mental Health'
		FINANCIAL_WEALTH = 'Financial Wealth', 'Financial Wealth'
		BALANCE_BETWEEN_ALL = 'Balance between All', 'Balance between All'

	category_name = models.CharField(
		max_length=35, choices=CategoryChoices.choices
	)