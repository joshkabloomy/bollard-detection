from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image_upload/', include('image_upload.urls')),  # Include your app's URLs
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # Add more top-level URLs here as needed
]
