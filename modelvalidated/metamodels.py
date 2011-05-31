from django.db import models
from exceptions import ValidationError


class ModelWithValidation(models.Model):

    def save(self, *args, **kw):
        self.validate()
        models.Model.save(self, *args, **kw)

    def validate(self):
        for field in self._meta.fields:
            meth_name = '_validate_' + field.name
            func = getattr(self, meth_name, None)
            if func and not func():
                msg = func.__doc__ or 'Field `%s` is not valid' % field.name
                raise ValidationError(msg)
