from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from .models import BlogPost

# Create your views here.


def index(request):
    latest_blogs = BlogPost.objects.order_by("-date")[:5]
    return render(request, "index.html", {"latest_blogs": latest_blogs})


def post_detail(request, primary_key):
    blog_post = get_object_or_404(BlogPost, pk=primary_key)
    return render(request, "post_detail.html", {"blog_post": blog_post})
