from django.shortcuts import render
from clean.models import Student
from django import forms


class EmpForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = "__all__"
        # fields = ['first_name','password']  #ab 2 hi field aenge
