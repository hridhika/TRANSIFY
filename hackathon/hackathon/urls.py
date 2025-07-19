# hackathon/hackathon/urls.py

from django.contrib import admin
from django.urls import path, include # <--- Make sure 'include' is imported
from django.views.generic import TemplateView # <--- Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'), # Simple home page
    path('', include('og.urls')), # <--- Include your app's URLs here
]
