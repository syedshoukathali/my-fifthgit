from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def syed(request):
    return HttpResponse('it is my surname')
def showkath(request):
    return HttpResponse('this is my name')