# shapes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.shape_view, name='shape_view'),
]
