from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from content.models import PostItem


def all_posts(request):
    posts = PostItem.objects.all()
    context = {'all_posts':posts}
    return render(request, 'content/all_post.html', context)


def post_detail(request, post_id):
    return HttpResponse(PostItem.objects.get(id=post_id))
