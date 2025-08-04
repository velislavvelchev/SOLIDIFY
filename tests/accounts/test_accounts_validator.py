from django.core.exceptions import ValidationError
from django.test import TestCase
from SOLIDIFY.accounts.validators import NameValidator


class TestNameValidator(TestCase):
    def setUp(self):
        self.validator = NameValidator(field_name='First name')

    def test_valid_name__success(self):
        valid_names = [
            'John',
            'Mary-Jane',
            'Anna Maria'
        ]

        for name in valid_names:
            try:
                self.validator(name)
            except ValidationError:
                self.fail(f"Validator failed for valid name: {name}")

    def test_invalid_name__error(self):
        invalid_names = [
            'John123',
            'Mary@Jane',
            '1234'
        ]

        for name in invalid_names:
            with self.assertRaises(ValidationError) as context:
                self.validator(name)
            self.assertEqual(
                str(context.exception),
                "['First name should contain only letters!']"
            )

    def test_name_with_whitespace__success(self):
        name = '  John  '
        try:
            self.validator(name)
        except ValidationError:
            self.fail("Validator failed for name with whitespace")