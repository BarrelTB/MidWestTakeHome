from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def return_home(request):
    return render(request, 'home.html')