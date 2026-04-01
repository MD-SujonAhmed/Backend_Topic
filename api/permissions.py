from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # শুধু অ্যাডমিন বা ব্লগের লেখক এডিট/ডিলিট করতে পারবে
        return request.user.role == 'admin' or obj.author == request.user