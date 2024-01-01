"""
URL configuration for Geography_Guesser project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('bollard_detection/upload/', views.opencv_image_upload, name='opencv_image_upload'),
    path('bollard_detection/success/', views.opencv_image_upload_success, name='opencv_image_upload_success'),
    path('bollard_recognition/upload/', views.yolo_image_upload, name='yolo_image_upload'),
    path('bollard_recognition/success/', views.yolo_image_upload_success, name='yolo_image_upload_success'),
]