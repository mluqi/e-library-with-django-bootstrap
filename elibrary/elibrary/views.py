# from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    # return HttpResponse("Hello World! Hello gan")
    return render(request, 'dashboard.html')

def category(request):
    # return HttpResponse("About Page")
    return render(request, 'category.html')

