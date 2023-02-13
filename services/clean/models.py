from django.db import models
from django import forms
from django.forms import ModelForm


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=30)
    contact=models.IntegerField(max_length=30)
    password=models.CharField(max_length=20)
    class Meta:
        db_table = "student"