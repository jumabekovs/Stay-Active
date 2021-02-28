from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from applications.blog.models import Post
from applications.club.models import Club


class HomepageView(ListView):
    model = Club
    template_name = 'index.html'
    context_object_name = 'clubs'

    def get_template_names(self):
        template_name = super(HomepageView, self).get_template_names()
        search = self.request.GET.get('search')
        if search:
            template_name = 'search.html'
        return template_name


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        if search:
            context['clubs'] = Club.objects.filter(Q(name__icontains=search) | Q(slug__icontains=search))
        else:
            context['clubs'] = Club.objects.all()
        return context




class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'


def blog_detail(request, sub_title):
    post = Post.objects.get(sub_title=sub_title)
    extends = post.comment.all()
    return render(request, 'blog_detail.html', locals())
