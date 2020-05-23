from django.urls import path
from . import views

urlpatterns = [
    # Paths services
    path('services/', views.services, name="services"),
    
]