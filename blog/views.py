from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here

def post_list(request):
    post = Post.objects.filter(published_date=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': post})


def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "blogdetail.html", {'post': post})
