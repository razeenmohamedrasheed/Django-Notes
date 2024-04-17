from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sampleResponse(request):
    return HttpResponse("hello")
