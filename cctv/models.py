from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(models.Model):
    user = models.OneToOneField(User)
    pos = models.CharField(max_length=20)
    phonenum = models.CharField(max_length=13)
