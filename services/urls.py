from django.urls import path
from . import views

urlpatterns = [
    # Paths 
    path('', views.services, name="services"),
    
]