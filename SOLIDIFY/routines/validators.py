from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RoutineNameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "Routine Name must contain only letters!"

    def __call__(self, value):
        # Remove leading/trailing spaces
        stripped = value.strip()

        # Split into words and check each word is alphabetic
        if not all(word.isalpha() for word in stripped.split()):
            raise ValidationError(self.message)
