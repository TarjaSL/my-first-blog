from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    AllPosts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': AllPosts})

def post_detail(request,pk):
    postN=get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html', {'postN': postN})
