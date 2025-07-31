from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .accounts.views import admin_logout_view
handler403 = 'SOLIDIFY.accounts.views.permission_denied_view'

urlpatterns = ([
    path('admin/logout/', admin_logout_view, name='admin-logout'),
    path('admin/', admin.site.urls),
    path('', include('SOLIDIFY.common.urls')),
    path('accounts/', include('SOLIDIFY.accounts.urls')),
    path('categories/', include('SOLIDIFY.categories.urls')),
    path('routines/', include('SOLIDIFY.routines.urls')),
    path('habits/', include('SOLIDIFY.habits.urls')),

    path('schedule/', include('SOLIDIFY.schedule.urls')),
])
               # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
