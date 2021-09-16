from django.shortcuts import render
from acme.helpers import (page, _render)
from .models import BlogPost

# Create your views here.


# /blog/<int:id> ex. http://localhost/blog/1
def blog_post_details_page(request, post_id):
  blogPosts = BlogPost.objects.get(id=post_id)
  context = {"post": blogPosts}

  return _render(request, 'blog_posts.index', context)
