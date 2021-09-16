from django.shortcuts import render

def page(request, name, context={}):
  return render(request, 'pages/{0}.jinja2'.format(name), context)
