from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated  # передал ли токен

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)


class IsRelationOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated  # передал ли токен

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)