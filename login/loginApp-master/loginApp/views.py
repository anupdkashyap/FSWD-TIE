import crypt
from hashlib import scrypt
from threading import activeCount
from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import crypt
from django .contriib .auth.models


def signup(request):
    return render(request, 'index2.html')

def login(reequest):
    return render(request,'insert.html')

def signup(request):
    if request.method=='POST':
        Create Account 
    else:
        return render(request):
    user=auth.authenticated