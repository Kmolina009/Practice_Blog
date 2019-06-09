from django.http import HttpResponse
#allows pages to be rendered
from django.shortcuts import render

def home(request):
    # return(request, 'home/')
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')