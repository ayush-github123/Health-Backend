from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Ensure only authors or admins can create a blog post
        if request.method == "POST":
            return getattr(request.user, 'is_author', False) or request.user.is_staff
        return True  # For other actions, object-level permission will apply

    def has_object_permission(self, request, view, obj):
        # Only the author or an admin can update or delete the post
        return getattr(request.user, 'is_author', False) or request.user.is_staff
