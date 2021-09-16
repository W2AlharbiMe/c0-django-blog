from django.shortcuts import render

def page(request, name, context={}):
  return render(request, 'pages/{0}.jinja2'.format(name), context)


def _render(request, name, context={}):
  folder, filename = name.split('.')
  return render(request, '{0}/{1}.jinja2'.format(folder, filename), context)
