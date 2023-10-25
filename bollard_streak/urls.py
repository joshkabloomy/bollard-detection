from django.urls import path
from . import views

urlpatterns = [
    path('', views.bollard_streak, name='bollard_streak'),
    
]