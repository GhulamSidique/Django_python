from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn(request):
    return HttpResponse("Would you like to learn python?")

def learn_lib(request):
    return HttpResponse("Here to teach you python libraries")