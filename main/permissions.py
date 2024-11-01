from rest_framework.permissions import BasePermission

class ISAdminBrothers(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Administraitors').exists()