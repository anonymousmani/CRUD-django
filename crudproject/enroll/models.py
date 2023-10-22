from django.db import models

# Create your models here.

class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)