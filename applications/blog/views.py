from django.shortcuts import render
from django.views.generic import ListView, DetailView

from applications.blog.models import Post


class HomepageView(ListView):
    model = Post
    template_name = 'index.html'


class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'


# class BlogDetailView(DetailView):
    # model = Post

def blog_detail(request, sub_title):
    post = Post.objects.get(sub_title=sub_title)
    extends = post.comment.all()
    return render(request, 'blog_detail.html', locals())
