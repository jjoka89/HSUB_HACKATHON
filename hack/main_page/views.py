import string
from django.shortcuts import render
from board.models import Post, Category

# Create your views here.
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:5]
    categories = Category.objects.all()
    return render(request, 'main.html',
                {
                    'recent_posts': recent_posts,
                    'categories' : categories
                }
    )