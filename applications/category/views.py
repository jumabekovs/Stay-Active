from django.views.generic import DetailView
from applications.category.models import CategoryClub, CategoryPost


class ClubCategoryDetailView(DetailView):
    model = CategoryClub
    template_name = 'club_category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['club_types'] = self.get_object().club_types.all()
        return context



class PostCategoryDetailView(DetailView):
    model = CategoryPost
    template_name = 'blog_category.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_category'] = self.get_object().post_category.all()
        return context


