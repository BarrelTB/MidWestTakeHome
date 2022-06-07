from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    path('', views.return_home, name='home'),
    path('contact/', views.return_contact, name='contact')
]