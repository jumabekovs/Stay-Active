from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.blog.urls')),
    path('clubs/', include('applications.club.urls')),
    path('offers/', include('applications.card.urls')),
    path('category/', include('applications.category.urls')),
    path('accounts/', include('applications.user.urls')),
    path('accounts/', include('allauth.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
