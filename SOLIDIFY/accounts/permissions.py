from django.core.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission

# allow permissions to api endpoints if the user is superuser or admin
class ApiPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        referer = request.META.get('HTTP_REFERER', '')

        # admin or superuser accessing whatever (calendar page/the api endpoints)
        if user.is_superuser or user.groups.filter(name='admin').exists():
            return True

        # user accessing their calendar events through the calendar and not the api endpoint
        if user.is_authenticated and '/calendar' in referer:
            return True

        raise PermissionDenied()
