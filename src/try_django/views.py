from django.http import HttpResponse

# internal company module
from acme.helpers import page

def home_page(request):
  languages = ["python", "javascript", "php"]
  context = {
    "languages": languages
  }

  return page(request, 'home', context)

def about_page(request):
 return page(request, 'about')

def contact_page(request):
 return page(request, 'contact')
