from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from SOLIDIFY.routines.models import Routine
from SOLIDIFY.categories.models import Category
from SOLIDIFY.habits.models import Habit
from django.contrib.auth import get_user_model

User = get_user_model()


class RoutineCreationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='routineuser@example.com',
            username='routineuser',
            password='password'
        )
        self.other_user = User.objects.create_user(
            email='other@example.com',
            username='otheruser',
            password='password'
        )
        self.category = Category.objects.create(
            user=self.user,
            category_type=Category.CategoryChoices.CREATIVE,
            description='Creative tasks'
        )
        self.habit = Habit.objects.create(
            user=self.user,
            habit_name='Draw',
            category=self.category
        )

    def test_create_valid_routine(self):
        """Test basic routine creation with all required fields"""
        routine = Routine.objects.create(
            user=self.user,
            routine_name='ArtSession',
            category=self.category
        )
        self.assertEqual(routine.routine_name, 'ArtSession')
        self.assertEqual(routine.user, self.user)
        self.assertEqual(routine.category, self.category)

    def test_create_routine_with_habits(self):
        """Test routine creation with associated habits"""
        routine = Routine.objects.create(
            user=self.user,
            routine_name='MorningRoutine',
            category=self.category
        )
        routine.habits.add(self.habit)
        self.assertEqual(routine.habits.count(), 1)
        self.assertIn(self.habit, routine.habits.all())

    def test_create_routine_without_habits(self):
        """Test routine can be created without habits"""
        routine = Routine.objects.create(
            user=self.user,
            routine_name='SoloRoutine',
            category=self.category
        )
        self.assertEqual(routine.habits.count(), 0)

    def test_unique_constraint_for_same_user(self):
        """Test same user cannot create duplicate routine names"""
        Routine.objects.create(
            user=self.user,
            routine_name='Workout',
            category=self.category
        )
        with self.assertRaises(IntegrityError):
            Routine.objects.create(
                user=self.user,
                routine_name='Workout',
                category=self.category
            )

    def test_unique_constraint_allows_different_users(self):
        """Test different users can have routines with same name"""
        Routine.objects.create(
            user=self.user,
            routine_name='EveningRoutine',
            category=self.category
        )
        other_category = Category.objects.create(
            user=self.other_user,
            category_type=Category.CategoryChoices.PHYSICAL
        )
        try:
            routine = Routine.objects.create(
                user=self.other_user,
                routine_name='EveningRoutine',
                category=other_category
            )
            self.assertEqual(routine.routine_name, 'EveningRoutine')
        except IntegrityError:
            self.fail("Different users should be allowed to have routines with same name")