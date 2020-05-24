from django.urls import path
from . import views

urlpatterns = [
    # Paths contact
    path('', views.contact, name="contact"),
    
]