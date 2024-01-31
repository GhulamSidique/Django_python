from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("<h1>Hello welcome to the django course</h1>")

def outline(request):
    return HttpResponse("This is the course outline")

def passing(request):
    a="these are the passing students"
    return HttpResponse(a)