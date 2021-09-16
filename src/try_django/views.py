from django.http import HttpResponse
from django.shortcuts import render

def page(request, name, context={}):
 return render(request, 'pages/{0}.jinja2'.format(name), context)

def home_page(request):
  return page(request, 'home')

def about_page(request):
 return page(request, 'about')

def contact_page(request):
 return page(request, 'contact')
