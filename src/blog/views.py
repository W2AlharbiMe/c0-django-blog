from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from acme.helpers import (page, _render)
from .models import BlogPost

# Create your views here.


# /blog/<int:id> ex. http://localhost/blog/1
def blog_post_details_page(request, post_id):
  post = get_object_or_404(BlogPost, id=post_id)
  context = {"post": post}

  return _render(request, 'blog_posts.index', context)
