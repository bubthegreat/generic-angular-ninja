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
from .models import (
    Employee,
    Department,
    KeyArea,
    Competency,
    FunctionalArea,
    Level,
    LevelDescription,
)
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore
from django.views.generic import TemplateView  # type: ignore
from skill_matrix_api.crud.utils import add_model_crud_route
from ninja.security import HttpBasicAuth
from django.contrib.auth.models import User
from ninja import Schema

# TODO: Remove this default admin/admin hack.
admins = User.objects.filter(is_staff=True)
if not admins:
    User(username='admin', password='admin', is_staff=True).save()

import time
UPTIME_START = time.time()

api = NinjaAPI()

# HACKY STATUS< DO THIS RIGHT

from django.db import connections
from django.db.utils import OperationalError


class StatusSchema(Schema):
    uptime: int
    mysql_connected: bool

@api.get('/status', response=StatusSchema)
def return_status(request):
    total_uptime = time.time() - UPTIME_START
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        mysql_connected = False
    else:
        mysql_connected = True

    return {'uptime': total_uptime, 'mysql_connected': mysql_connected}

add_model_crud_route(api, "employees", Employee)
add_model_crud_route(api, "departments", Department)
add_model_crud_route(api, "keyarea", KeyArea)
add_model_crud_route(api, "competency", Competency)
add_model_crud_route(api, "functonalarea", FunctionalArea)
add_model_crud_route(api, "level", Level)
add_model_crud_route(api, "leveldescription", LevelDescription)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


