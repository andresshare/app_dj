from django.shortcuts import render
from django.lphttp import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Message")
