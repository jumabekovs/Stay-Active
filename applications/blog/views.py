from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import View

from applications.blog.forms import SendWishesForm
from applications.blog.models import Post
from applications.club.models import Club
from project import settings


class HomepageView(ListView):
    model = Club
    template_name = 'applications/index.html'
    context_object_name = 'clubs'




class BlogView(ListView):
    model = Post
    template_name = 'applications/blog.html'
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
    return render(request, 'applications/blog_detail.html', locals())


# def send_wishes(request, *args, **kwargs):
#     name = request.POST.get('Name', '')
#     email = request.POST.get('Email', '')
#     subject = request.POST.get('Subject',)
#     message = request.POST.get('Message',)
#     if request.method == 'POST':
#         send_mail(subject, message, settings.EMAIL_HOST_USER, ['azamatjumma@gmail.com'], fail_silently=False)
#     return render(request, 'accounts/order_form.html', locals())


class SendWishes(FormView):
    template_name = 'applications/contact.html'
    form_class = SendWishesForm
    success_url = 'home/'

    def form_valid(self, form):
        form.send_wishes()
        return super().form_valid(form)