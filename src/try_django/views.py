from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
  return render(request, 'home.html')


def about_page(request):
 return HttpResponse("<h1>About Page</h1>")

def contact_page(request):
 return HttpResponse("<h1>Contact Page</h1>")