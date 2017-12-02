from django.db import models

# Create your models here.
class Manager(models.Model):
    id = models.CharField(max_length=20, primary_key=True, null=False)
    pw = models.CharField(max_length=20, null=False)
    pos = models.CharField(max_length=20)
    phonenum = models.CharField(max_length=13)
