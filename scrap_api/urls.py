"""scrap_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from django.contrib import admin
from django.urls import path

from api.views import ProductViewSet, PageScrappingViewSet

api_v1 = routers.DefaultRouter(trailing_slash=False)
api_v1.register(r'product', ProductViewSet, basename='product')
api_v1.register(r'page-scraping', PageScrappingViewSet, basename='pagescrap')

urlpatterns = [
    url(r'v1/', include(api_v1.urls))
]
