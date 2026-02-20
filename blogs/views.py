from django.shortcuts import render
from .models import Blog, Tag
from products.models import Category


def blogs_list_view(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_posts = Blog.objects.order_by('-created_at')[:3]

    context = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts,
    }
    return render(request, 'blogs/blogs-list.html', context)