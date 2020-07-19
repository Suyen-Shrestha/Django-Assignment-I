from django.shortcuts import render, get_object_or_404
from .models import Author, BlogPost



def home(request):
    return render(request, 'blog/home.html')


def blogsList(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }

    return render(request, 'blogapp/bloglist.html', context)


def blogDetail(request,blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    context = {
        'blog': blog
    }

    return render(request, 'blogapp/blogdetail.html', context)

