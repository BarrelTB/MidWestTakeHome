from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def return_contact_home(request):
    return render(request, 'contact.html')