from django.core.validators import ValidationError
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

    def __str__(self):
        return "%d" % self.pk

    def to_dict(self):
        data = {}
        for f in self._meta.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data