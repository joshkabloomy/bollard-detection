from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('opencv_detection/', include('image_upload.urls')), 
    path('', include('home.urls')),
    path('bollard_streak/', include('bollard_streak.urls'))
    
    
     # Include your app's URLs
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # Add more top-level URLs here as needed
]
