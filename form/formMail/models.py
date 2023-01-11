from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MedicalStudents(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    college=models.CharField(max_length=100)
    med=models.CharField(max_length=10)

class EngineerStudents(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    college=models.CharField(max_length=100)
    eng=models.CharField(max_length=10)


