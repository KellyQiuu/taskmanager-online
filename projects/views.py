#views.py
from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee,Projects
from .forms import ProjectFormSet, ProjectForm
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Employee

from buzy.serializers import EmployeeSerializer

# Create your views here.
def create_project(request, pk): 
    employee = Employee.objects.get(pk=pk)
    form = ProjectForm(request.POST or None)
    projects = Projects.objects.filter(employee=employee)

    if request.method == "POST": 
        if form.is_valid(): 
            project = form.save(commit=False)
            project.employee = employee
            project.save()
            return redirect("detail-form", pk=project.id)
        else: # there is an error on the form 
            return render(request, "partials/project_form.html", {"form": form})
    context = {
        "form": form,
        "employee": employee,
        "projects":projects
    }
    # if the form don't successfully return a project, it will 
    # redirect to this render
    return render(request, "create_project.html", context)


def create_project_form(request): 
    context = {"form": ProjectForm()}
    return render(request, "partials/project_form.html",context)


def project_detail(request, pk): 
    project = Projects.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "partials/project_detail.html",context)




def employee_projects(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    projects = Projects.objects.filter(employee=employee)
    total_work = 0
    
    projects_completed = projects.filter(current_stage= 'Completed')
    projects_ongoing = projects.exclude(current_stage= 'Completed').exclude(current_stage='Paused')
    for p in projects_ongoing:
        total_work += p.time_occupancy

    context = {
        'employee': employee,
        'projects': projects,
        'workload': total_work,
        'ongoing': projects_ongoing,
        'archive':projects_completed
        
    }
 
    return render(request, 'list_projects.html', context)

@login_required
def homepage(request):
    employees = Employee.objects.all()
    selected_department = request.GET.get('department')
    if selected_department:
        employees = Employee.objects.filter(department=selected_department)
    else:
        employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'homepage.html', context)

@login_required
def search_view(request): 
    query = request.GET.get('query')
    employees=Employee.objects.all()
    if query: 
        employees = Employee.objects.filter(legal_name__icontains=query)

    empty=False

    if not employees:
        empty = True
    context = {
        'employees': employees,
        'query': query,
        'empty':empty
    }
    return render(request, 'homepage.html', context)

@login_required
def delete_project(request, pk):
    project = Projects.objects.get(pk=pk)
    
    project.delete()

    return HttpResponse('')


@login_required
def updated_project(request, pk):
    project = Projects.objects.get(pk=pk)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST": 
        if form.is_valid():
            project = form.save()
            return redirect("detail-form", pk=project.id)

    context = {
        "form": form,
        "project":project
    }

    return render(request, "partials/project_form.html", context)





def update_project(request, pk):
    employee = Employee.objects.get(pk=pk)
    projects = Projects.objects.filter(employee=employee)
     # For other POST requests, handle project form submission
    form = ProjectForm(request.POST)
    if request.method == "POST":
        # If the request is a DELETE request, delete the project
        if request.POST.get("_method") == "delete":

            if form.is_valid():
                project = form.save(commit=False)
                project.employee = employee
                project.save()
                return redirect("detail-form", pk=project.id)
            else:
                return render(request, "partials/project_form.html", {"form": form})

    # For GET requests, render the update_project.html template with the project list
    context = {
        "form": ProjectForm(),
        "employee": employee,
        "projects": projects,
    }
    return render(request, "update_project.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to the homepage after successful login
        else:
            # Invalid credentials, show an error message to the user
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


class EmployeeViewSet(CreateModelMixin,RetrieveModelMixin, UpdateModelMixin,GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def department_search(request): 


    pass
