from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #get request pathabe. eita genaler user er khetre
            return True
        else: # put, delete, post . ar eita hoche admin ar staf er khetre
            bool(request.user and request.user.is_staff)

class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user
    