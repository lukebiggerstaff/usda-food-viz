from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('search', views.Search.as_view(), name='search'),
]
