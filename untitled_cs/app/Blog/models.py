from django.db import models
from app.user.models import User

# Create your models here.


class BlogInfo(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    Buser = models.ForeignKey('user.User')

    def __str__(self):
        return "%d" % self.pk

