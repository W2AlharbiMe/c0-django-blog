from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
  page_title = 'Home Page'
  return render(request, 'home.jinja2', {"title": page_title})


def about_page(request):
 return HttpResponse("<h1>About Page</h1>")

def contact_page(request):
 return HttpResponse("<h1>Contact Page</h1>")