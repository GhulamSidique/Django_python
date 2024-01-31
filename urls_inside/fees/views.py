from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def py_fees(request):
    return HttpResponse("Would you like to learn js?")

def py_lib_fees(request):
    return HttpResponse("Here to teach you js libraries")
