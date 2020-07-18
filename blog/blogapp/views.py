from django.shortcuts import render
from .models import Author, BlogPost


def blogsList(request):
    blogs = BlogPost.objects.all()
    context = {
        'blogs': blogs
    }

    return render(request, 'blogapp/bloglist.html', context)

