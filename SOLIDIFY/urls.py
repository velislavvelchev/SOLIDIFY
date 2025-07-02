from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
       path('admin/', admin.site.urls),
    path('', include('SOLIDIFY.common.urls')),
    path('accounts/', include('SOLIDIFY.accounts.urls')),
    path('categories/', include('SOLIDIFY.categories.urls')),
    path('routines/', include('SOLIDIFY.routines.urls')),
    path('habits/', include('SOLIDIFY.habits.urls')),

    path('schedule/', include('SOLIDIFY.schedule.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
