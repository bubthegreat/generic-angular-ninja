"""skill_matrix_api URL Configuration

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
from django.urls import path  # type: ignore
from ninja import NinjaAPI
from .models import Employee, Department, KeyArea, Competency, FunctionalArea, Level, LevelDescription
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore
from django.views.generic import TemplateView  # type: ignore
from skill_matrix_api.crud.utils import add_model_crud_route

api = NinjaAPI()

add_model_crud_route(api, 'employees', Employee)
add_model_crud_route(api, 'departments', Department)
add_model_crud_route(api, 'keyarea', KeyArea)
add_model_crud_route(api, 'competency', Competency)
add_model_crud_route(api, 'functonalarea', FunctionalArea)
add_model_crud_route(api, 'level', Level)
add_model_crud_route(api, 'leveldescription', LevelDescription)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path('', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
