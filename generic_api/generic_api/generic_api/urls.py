"""generic_api URL Configuration

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
import asyncio

from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from ninja import NinjaAPI
from .models import (
    StringConfig,
    IntConfig,
    UserProfile,
)
from django.conf.urls.static import static  # type: ignore
from django.conf import settings  # type: ignore
from django.views.generic import TemplateView  # type: ignore
from generic_api.crud.utils import add_model_crud_route
from ninja.security import HttpBasicAuth
from django.contrib.auth.models import User
from ninja import Schema

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

@api.get('/load')
async def load_generate(request):
    x = 2
    count = 0
    while count < 18:
        x = x * x
        count += 1
    
    await asyncio.sleep(0.1)
    return x


add_model_crud_route(api, "string_configs", StringConfig)
add_model_crud_route(api, "int_configs", IntConfig)
add_model_crud_route(api, "user_profile", UserProfile)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


