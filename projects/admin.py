from django.contrib import admin
from .models import Employee,Projects,User

# Register your models here.
class ProjectInlineAdmin(admin.TabularInline): 
    model = Projects
    


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [ProjectInlineAdmin]

admin.site.register(Employee,EmployeeAdmin)

