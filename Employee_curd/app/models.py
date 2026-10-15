from django.db import models

# Create your models here.

class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    gender_choices=(('male','MALE'),('female','FEMALE'))
    gender=models.CharField(max_length=10,choices=gender_choices)
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    joining_date=models.DateField(auto_now_add=True)


