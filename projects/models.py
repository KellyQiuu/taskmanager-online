from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User




STAGE_CHOICE = ( ('Planning', 'Planing'),
    ('Started', 'Started'),
    ('Pending', 'Pending'),
    ('Submitted', 'Submitted'),
    ('Approved', 'Approved'),
    ('Completed', 'Completed'),
    ('Paused', 'Paused')
    # Add more options as needed
)

DEPARTMENTS = (
    ('RTR', 'RTR'), 
    ('PTP','PTP'), 
    ('CI', 'CI'), 
    ('IC', 'IC'), 
    ('TE','TE'),
    ('IT','IT'),
    ('support team','support team'),
    ('None','None')
)
# Create your models here.
class Employee(models.Model): 
    legal_name = models.CharField(max_length=128)
    english_name = models.CharField(max_length=128)
    email = models.EmailField()
    gid = models.CharField(max_length=50)
    grade = models.SmallIntegerField()
    title = models.CharField(max_length=128)
    hire_date = models.DateField()
    department = models.CharField(max_length=50, choices=DEPARTMENTS, null = True)

    def __str__(self) -> str:
        return self.legal_name
    
class Projects(models.Model): 
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    project_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    manager = models.CharField(max_length=128)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    current_stage = models.CharField(max_length=55,choices=STAGE_CHOICE)
    time_occupancy = models.IntegerField()
    
    def __str__(self) -> str:
        return self.project_name
    


# Your existing code for STAGE_CHOICE, Employee, and Projects models

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    legal_name = models.CharField(max_length=128)
    english_name = models.CharField(max_length=128)
    gid = models.CharField(max_length=50)
    grade = models.SmallIntegerField()
    title = models.CharField(max_length=128)
    hire_date = models.DateField()

    def __str__(self) -> str:
        return self.legal_name + '  ' + self.title
