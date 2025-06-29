from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, field_name, message=None):
        self.field_name = field_name
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or f'{self.field_name} should contain only letters!'

    def __call__(self, value):
        stripped = value.strip().replace('-', '')

        if not all(word.isalpha() for word in stripped.split()):
            raise ValidationError(self.message)

