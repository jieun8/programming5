from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from blog.models import Post

def intro(request):
    return render(request, 'blog/index.html', {})


def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')[:10]
    return render(request, 'blog/post_list.html', {'post_list' : post_list})


def post_add(request):
    return render(request, 'blog/post_add.html', {})


def post_upload(request):
    post_title = request.POST['title']
    post_text = request.POST['text']
    post_new = Post()
    post_new.title = post_title
    post_new.text = post_text
    post_new.save()
    return HttpResponseRedirect(reverse('post:post_list', args=''))


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post' : post})