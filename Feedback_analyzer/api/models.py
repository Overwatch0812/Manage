from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=25)
    contact=models.CharField(max_length=10)
    Address=models.CharField(max_length=50)
    course=models.CharField(max_length=15)

