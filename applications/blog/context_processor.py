from applications.category.models import CategoryPost


def get_post_category(request):
    post_categories = CategoryPost.objects.filter(parent__isnull=True)
    return {'post_categories': post_categories}

