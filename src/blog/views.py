from django.http.response import Http404
from django.shortcuts import render
from acme.helpers import (page, _render)
from .models import BlogPost

# Create your views here.


# /blog/<int:id> ex. http://localhost/blog/1
def blog_post_details_page(request, post_id):
  try:
    blogPosts = BlogPost.objects.get(id=post_id)
  except:
    raise Http404

  context = {"post": blogPosts}

  return _render(request, 'blog_posts.index', context)
