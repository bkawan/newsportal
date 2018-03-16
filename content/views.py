from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from content.models import PostItem, Category


def all_posts(request):
    posts = PostItem.objects.all()
    categories = Category.objects.all()
    context = {'all_posts':posts}
    return render(request, 'content/all_post.html', context)


class HomePageView(TemplateView):
    template_name = 'content/all_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_posts'] = PostItem.objects.all().order_by('-published_date')
        context['categories'] = Category.objects.all()
        return context


def post_detail(request, post_id):
    return HttpResponse(PostItem.objects.get(id=post_id))


def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = PostItem(
            title=title,
            content=content,
        )
        post.save(status="published")
        return redirect('index')

    context = {
    }
    return render(request, 'content/post_create.html', context)
