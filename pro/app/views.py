from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#function based

def Home(request):
    if(request.method=="GET"):
        return HttpResponse("Welcome to Django")

def index(request):
    if(request.method=="GET"):
        return HttpResponse("Index")