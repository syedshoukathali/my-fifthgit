from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('it is app1 first view')
def second(request):
    return HttpResponse('this is app1 second view')