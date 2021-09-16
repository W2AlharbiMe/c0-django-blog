from django.db.models.query import QuerySet
from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from acme.helpers import (page, _render)
from .models import BlogPost

# Create your views here.

def blog_post_list_view(request):
  context = {"posts": []}
  template_name = 'blog_posts.index'

  return _render(request, template_name, context)


# /blog/<str:slug> ex. http://localhost/blog/my-first-post/
def blog_post_show_page(request, slug):
  post = get_object_or_404(BlogPost, slug=slug)
  context = {"post": post}
  template_name = 'blog_posts.show'

  return _render(request, template_name, context)

def blog_post_create_view(request):
  context = {"posts": []}
  template_name = 'blog_posts.create'

  return _render(request, template_name, context)


def blog_post_edit_view(request):
  context = {"posts": []}
  template_name = 'blog_posts.edit'

  return _render(request, template_name, context)



# delete will be done via ajax
def blog_post_delete_view(request):
  pass


