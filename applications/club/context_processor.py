from applications.category.models import CategoryClub


def get_club_category(request):
    club_categories = CategoryClub.objects.filter(parent__isnull=True)
    return {'club_categories': club_categories}