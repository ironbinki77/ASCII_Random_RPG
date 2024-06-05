from django.urls import path
from . import views
from .views import battle_view

urlpatterns = [
    path('', views.main, name='main'),
    path('battle/', battle_view, name='battle_view'),
]