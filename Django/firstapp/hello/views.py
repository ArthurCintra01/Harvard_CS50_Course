from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def arthur(request):
    return HttpResponse("Hello, Arthur!")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })