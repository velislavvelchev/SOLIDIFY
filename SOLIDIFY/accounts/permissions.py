from django.core.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission

class ApiPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        referer = request.META.get('HTTP_REFERER', '')
        if user.is_superuser or user.groups.filter(name='admin').exists():
            return True

        if user.is_authenticated and '/calendar' in referer:
            return True

        raise PermissionDenied()
