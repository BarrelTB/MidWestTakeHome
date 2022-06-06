from django.urls import path
from . import views

#URLConfModule
urlpatterns = [
    path('contact/', views.return_contact_home)
]