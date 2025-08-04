from django.db import IntegrityError
from django.test import TestCase
from SOLIDIFY.habits.models import Habit
from SOLIDIFY.categories.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


class HabitCreationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='habituser@example.com',
            username='habituser',
            password='password'
        )
        self.other_user = User.objects.create_user(
            email='other@example.com',
            username='otheruser',
            password='password'
        )
        self.category = Category.objects.create(
            user=self.user,
            category_type=Category.CategoryChoices.MENTAL,
            description='Mindful tasks'
        )
        self.other_category = Category.objects.create(
            user=self.other_user,
            category_type=Category.CategoryChoices.PHYSICAL
        )

    def test_create_valid_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            habit_name='Meditate',
            category=self.category,
            dopamine_type=Habit.HabitChoices.ANTICIPATORY,
            priority=2
        )
        self.assertEqual(habit.habit_name, 'Meditate')
        self.assertFalse(habit.is_completed)
        self.assertEqual(habit.priority, 2)
        self.assertEqual(habit.dopamine_type, 'Anticipatory')

    def test_default_priority_and_completion(self):
        habit = Habit.objects.create(
            user=self.user,
            habit_name='Read book',
            category=self.category
        )
        self.assertEqual(habit.priority, 1)
        self.assertFalse(habit.is_completed)

    def test_unique_habit_name_per_user(self):
        """Test that same user cannot create duplicate habit names"""
        Habit.objects.create(
            user=self.user,
            habit_name='Meditation',
            category=self.category
        )

        with self.assertRaises(IntegrityError):
            Habit.objects.create(
                user=self.user,
                habit_name='Meditation',
                category=self.category
            )

    def test_same_habit_name_allowed_for_different_users(self):
        """Test that different users can have habits with same name"""
        Habit.objects.create(
            user=self.user,
            habit_name='Reading',
            category=self.category
        )

        # This should not raise an error
        habit = Habit.objects.create(
            user=self.other_user,
            habit_name='Reading',
            category=self.other_category
        )
        self.assertEqual(habit.habit_name, 'Reading')

    def test_unique_constraint_with_different_categories(self):
        """Test that same user can't have same habit name even with different categories"""
        Habit.objects.create(
            user=self.user,
            habit_name='Exercise',
            category=self.category
        )

        new_category = Category.objects.create(
            user=self.user,
            category_type=Category.CategoryChoices.PHYSICAL
        )

        with self.assertRaises(IntegrityError):
            Habit.objects.create(
                user=self.user,
                habit_name='Exercise',
                category=new_category
            )