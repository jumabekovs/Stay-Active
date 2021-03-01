from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from applications.blog.models import Post
from applications.club.models import Club


class HomepageView(ListView):
    model = Club
    template_name = 'index.html'
    context_object_name = 'clubs'




class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['recently'] = Post.objects.all().order_by('-created_date')[:2]
        return context


def blog_detail(request, sub_title):
    post = Post.objects.get(sub_title=sub_title)
    extends = post.comment.all()
    recently = Post.objects.all().order_by('-created_date')[:3]
    return render(request, 'blog_detail.html', locals())


