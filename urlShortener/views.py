from django.shortcuts import render
from django.http import HttpResponse

# def homePage(request):
#     return render ( request, 'home/index.html')

def task(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def aboutUS(request):
    return HttpResponse("welcome")

def course(request):
    return HttpResponse("welcome to coures")