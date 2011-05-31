import unittest
from fake_models import FakePerson
from exceptions import ValidationError


class TestValidation(unittest.TestCase):

    def test_valid_model(self):
        self.should_be_valid({'name': 'person1', 'age': 10})

    def test_invalid_age(self):
        self.should_not_be_valid({'name': 'person1', 'age': -1},
                                 "age must be greater than zero")

    def test_invalid_name(self):
        self.should_not_be_valid({'name': 'cant contain `foo`', 'age': 10},
                                 "name cant contain substring `foo`")

    def test_invalid_field_with_no_docstring(self):
        self.should_not_be_valid({'name': 'valid name',
                                  'age': 10, 'surname': '123'},
                                 "Field `surname` is not valid")
        

    def should_be_valid(self, kwargs):
        try:
            FakePerson.objects.create(**kwargs)
        except ValidationError, e:
            assert False, e

    def should_not_be_valid(self, kwargs, validation_msg=''):
        default_msg = "Expected FakePerson(%s) to be invalid" % kwargs
        try:
            FakePerson.objects.create(**kwargs)
        except ValidationError, e:
            if validation_msg:
                self.assertEquals(e.args, (validation_msg,))
        else:
            assert False, default_msg
