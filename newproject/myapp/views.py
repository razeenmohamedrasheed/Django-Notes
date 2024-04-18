from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sampleResponse(request):
    userData={
        "name" :"Razeen mohamed Rasheed",
        "email":"razeen rasheed 83@gmaail.com",
        "age":25,
        "status":'failed'

    }
    return render(request,'index.html',userData)
