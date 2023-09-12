from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Others'),
    )
    DEPARTMENT_CHOICES = (
        ('CS', 'COMPUTER SCIENCE'),
        ('C', 'COMMERCE'),
        ('E', 'ENGLISH'),
        ('M', 'MATHS'),
        ('S', 'SOCIAL SCIENCE'),
    )
    name=models.CharField(max_length=250,unique=True)
    dob=models.DateField(max_length=8)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()

    class Meta:
        ordering=('name',)
        verbose_name='student'
        verbose_name_plural='students'

    def __str__(self):
        return self.name





