from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'search', views.SearchViewSet, "food-list")
router.register(r'food', views.FoodViewSet, "food-detail")

urlpatterns = [
    path('', include(router.urls)),
]
