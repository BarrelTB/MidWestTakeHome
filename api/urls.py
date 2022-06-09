from django.urls import path
from . import views


urlpatterns = [
    path('loremipsum/', views.get_lorem_ipsum_content),
    path('submitcontact/', views.post_contact_message)
]