from django.urls import path
from . import views

urlpatterns = [
    # Paths 
    path('<int:page_id>/', views.page, name="page"),
]
    