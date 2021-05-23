#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
   
    return render(request, 'yellowpage/home.html')

def login(request):
    username = "not logged in"

    return render(request, 'yellowpage/login.html')
   
    if request.method == "POST":
          #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()
		
    return render(request, 'yellowpage/loggedin.html', {"username" : username})    