from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin' or obj.author == request.user