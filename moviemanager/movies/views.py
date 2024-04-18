from django.shortcuts import render

# Create your views here.

def createMovie(request):
    return render(request,'create.html')

def editMovie(request):
    return render(request,'edit.html')

def listMovie(request):
    return render(request,'list.html')