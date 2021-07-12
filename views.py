from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db import connection

def homepage(request):
    return render(request,'alertprodsite/homepage.html')