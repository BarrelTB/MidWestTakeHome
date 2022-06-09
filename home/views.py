from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def return_home(request):
    endpoint = 'http://localhost:8000/api/loremipsum/'
    get_response = requests.get(endpoint)
    data = json.loads(get_response.text)
    return render(request, 'home.html', {'listData': data})

def return_contact(request):
    return render(request, 'contact.html')

