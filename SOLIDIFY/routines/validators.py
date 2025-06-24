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
        if not value.isalpha():
            raise ValidationError(self.message)