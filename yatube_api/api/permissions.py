from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user

    def get_permissions(self):
        if self.action == 'retrieve':
            return (IsOwnerOrReadOnly(),)

        return super().get_permissions()
