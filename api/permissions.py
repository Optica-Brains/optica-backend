from rest_framework import permissions


class IsManagerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        user_is_from_branch = request.data['branch'] == request.user.branch_id
        manager_group = 1
        return user_is_from_branch and request.user.is_in_group(manager_group)
