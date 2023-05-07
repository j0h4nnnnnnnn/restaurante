"""opinionRestaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from django.urls import re_path
from appComentatioRestaurante.View import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
 openapi.Info(
title="API para predecir el tipo de comentario en un restaurante",
default_version='v1',
description="Es el API para predicción de crédito en una institución financiera",
terms_of_service="https://www.google.com/policies/terms/",
license=openapi.License(name="BSD License"),
 ),
 public=True,
 permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
path('admin/', admin.site.urls),
re_path(r'^nuevasolicitud/$',views.Clasificacion.determinarCategoria),
re_path(r'^predecir/',views.Clasificacion.predecir),
re_path(r'^predecirIOJson/',views.Clasificacion.predecirIOJson),
path('admin/', admin.site.urls),
path('', views.home, name='home')
]
"""""
urlpatterns = [
url(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
path('admin/', admin.site.urls),
url(r'^nuevasolicitud/$',views.Clasificacion.determinarCategoria),
url(r'^predecir/',views.Clasificacion.predecir),
url(r'^predecirIOJson/',views.Clasificacion.predecirIOJson),
path('admin/', admin.site.urls),
path('', views.home, name='home')
]
#urlpatterns = [
 #   path('admin/', admin.site.urls),
#]
"""