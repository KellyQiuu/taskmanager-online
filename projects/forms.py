# forms.py
from django import forms
from .models import Projects, Employee
from django.forms.models import inlineformset_factory

class ProjectForm(forms.ModelForm): 
    class Meta: 
        model = Projects
        fields = {
            "employee",
            "project_name",
            "description",
            "manager",
            "start_date",
            "end_date",
            "current_stage",
            "time_occupancy"
        }

ProjectFormSet = inlineformset_factory(Employee, 
    Projects,
    ProjectForm,
    can_delete=True,
    min_num = 1,
    extra = 0)
