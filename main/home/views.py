from django.shortcuts import render
from django import views
from django.http import HttpResponse
# Create your views here.

class Home(views.View):
    def get(self, request):
        return HttpResponse('This is the home page with a GET request <h1> this is the greatest </h1>')
    
    
