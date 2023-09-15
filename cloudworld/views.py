from django.shortcuts import render
from django.http import  HttpResponse
from cloudworld import models

# Create your views here.

def index(request):
    response = render(request,'index.html')
    developed_by = "Suraj Shaw"
    employee = models.Emp.objects.all()

    context = {
        "developer" : developed_by,
        "employee" : employee
    }

    response = render(request,'index.html',context)
    return response
