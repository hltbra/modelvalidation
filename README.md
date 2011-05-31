Django Model Validation (proof of concept)
==========================================


The goal of is to be able to specify, easily,
model validation. Like:

    from django.db import models
    from metamodels import ModelWithValidation


    class FakePerson(ModelWithValidation):

        name = models.CharField(max_length=255)
        age = models.IntegerField()
        
        def _validate_age(self):
            "age must be greater than zero"
            return self.age > 0

