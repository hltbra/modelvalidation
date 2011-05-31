from django.db import models
from metamodels import ModelWithValidation


class FakePerson(ModelWithValidation):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def _validate_age(self):
        "age must be greater than zero"
        return self.age > 0

    def _validate_name(self):
        "name cant contain substring `foo`"
        return 'foo' not in self.name

    def _validate_surname(self):
        return '123' not in self.surname