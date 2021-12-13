from django.db import models

# Create your models here.
class Clock(models.Model):
    second = models.IntegerField()
    user = models.CharField(max_length=100, blank=True,null=True)