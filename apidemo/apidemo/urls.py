"""apidemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore
from django.urls import path  # type: ignore
from ninja import NinjaAPI
from .types import EmployeePost, DepartmentPost, EmployeeGet, DepartmentGet
from .models import Employee, Department
from typing import List
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore
from .views import HomePageView
from django.views.generic import TemplateView  # type: ignore


api = NinjaAPI()

@api.post("/employees")
def create_employee(request, payload: EmployeePost):
    """Create a new employee based on input."""
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}

@api.get("/employees/{employee_id}", response=EmployeeGet)
def get_employee(request, employee_id: int):
    """Return an object for the employee ID specified."""
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

@api.get("/employees", response=List[EmployeeGet])
def list_employees(request):
    """Return a list of all employees."""
    qs = Employee.objects.all()
    return qs

@api.post("/departments")
def create_department(request, payload: DepartmentPost):
    """Create a new department based on input."""
    department = Department.objects.create(**payload.dict())
    return {"id": department.id}

@api.get("/departments/{department_id}", response=DepartmentGet)
def get_department(request, department_id: int):
    """Return an object for the department ID specified."""
    department = get_object_or_404(Department, id=department_id)
    return department

@api.get("/departments", response=List[DepartmentGet])
def list_departments(request):
    """Return a list of all departments."""
    qs = Department.objects.all()
    return qs

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path('', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
