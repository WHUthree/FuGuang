from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # 管理员
        if request.user.is_superuser:
            return True

        return obj == request.user

