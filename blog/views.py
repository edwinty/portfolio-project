from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def allblogs(request):
    point = Article.objects
    return render(request, 'blog/allblogs.html', {'articles': point})

def detail(request, blog_id):
    detailblog = get_object_or_404(Article, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})