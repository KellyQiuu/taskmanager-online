from django.contrib import admin
from django.urls import path,include
from projects import views
from rest_framework import routers
from projects.views import EmployeeViewSet


from projects.views import (create_project, create_project_form,
                            employee_projects, homepage,
                            search_view, 
                            project_detail,delete_project,
                            updated_project,login_view)

router = routers.DefaultRouter()
router.register('employee', views.EmployeeViewSet)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('htmx/project-form/', create_project_form, name='project-form'),
    path('htmx/project/<int:pk>/', project_detail, name='detail-form'),
    path('<int:pk>/',create_project, name="create-project"),
    path('employee/<int:employee_id>/', 
         employee_projects, name='employee-projects'),
    path('search/', search_view, name='search'),
    path('htmx/project/<int:pk>/delete/', delete_project, name='delete-project'),
    path('htmx/project/<int:pk>/update/', updated_project, name='update-project'),
    path('login/', login_view, name='login'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include(router.urls)),
     
]
