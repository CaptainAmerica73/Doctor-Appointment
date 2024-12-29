from datetime import time
from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.username
    
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=[('M','male'),('F','female'),('O','other')],max_length=1)
    age = models.PositiveIntegerField()
    specialization = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()
    location = models.TextField()
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    registration_no = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name