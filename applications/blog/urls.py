from django.urls import path

from applications.blog.views import HomepageView, BlogView, blog_detail, SendWishes  # BlogDetailView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<str:sub_title>/', blog_detail, name='blog-detail'),
    path('send-wishes/', SendWishes.as_view(), name='wishes'),
]