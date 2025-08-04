from django.test import TestCase
from django.core.exceptions import ValidationError
from SOLIDIFY.routines.validators import RoutineNameValidator


class RoutineNameValidatorTests(TestCase):
    def setUp(self):
        self.validator = RoutineNameValidator()

    def test_valid_names_pass(self):
        valid_names = [
            'MorningRoutine',
            'Workout',
            'Yoga',
            'Meditation',
            'Reading'
        ]

        for name in valid_names:
            with self.subTest(name=name):
                try:
                    self.validator(name)
                except ValidationError:
                    self.fail(f"Validator failed for valid name: {name}")

    def test_invalid_names_fail(self):
        """Test that names with invalid characters fail"""
        invalid_names = [
            'Morning123',  # Numbers
            'Workout@Gym',  # Special chars
            'Routine_One',  # Underscore
            'Hello!',  # Punctuation
            'Hello-World',  # Hyphen
        ]

        for name in invalid_names:
            with self.subTest(name=name):
                with self.assertRaises(ValidationError):
                    self.validator(name)

    def test_error_message(self):
        """Test that the correct error message is returned"""
        with self.assertRaises(ValidationError) as context:
            self.validator("Invalid123")

        self.assertEqual(
            str(context.exception),
            "['Routine Name must contain only letters!']"
        )