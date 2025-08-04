from django.test import TestCase
from django.db import IntegrityError
from SOLIDIFY.categories.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryCreationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='catuser@example.com',
            username='catuser',
            password='password'
        )
        self.other_user = User.objects.create_user(
            email='otheruser@example.com',
            username='otheruser',
            password='password'
        )

    def test_create_valid_category(self):
        category = Category.objects.create(
            user=self.user,
            category_type=Category.CategoryChoices.MENTAL,
            description='Mindfulness activities',
            min_habits_per_day=2
        )
        self.assertEqual(str(category), 'Mental')
        self.assertEqual(category.user, self.user)
        self.assertEqual(category.min_habits_per_day, 2)

    def test_default_min_habits(self):
        category = Category.objects.create(
            user=self.user,
            category_type=Category.CategoryChoices.PHYSICAL
        )
        self.assertEqual(category.min_habits_per_day, 1)

    def test_unique_constraint_for_same_user(self):
        """Test that same user cannot create duplicate category types"""
        Category.objects.create(
            user=self.user,
            category_type=Category.CategoryChoices.FINANCIAL
        )

        with self.assertRaises(IntegrityError):
            Category.objects.create(
                user=self.user,
                category_type=Category.CategoryChoices.FINANCIAL
            )

    def test_unique_constraint_allows_different_users(self):
        """Test that different users can have same category type"""
        Category.objects.create(
            user=self.user,
            category_type=Category.CategoryChoices.CREATIVE
        )

        # This should not raise an error
        category = Category.objects.create(
            user=self.other_user,
            category_type=Category.CategoryChoices.CREATIVE
        )
        self.assertEqual(category.category_type, 'Creative')