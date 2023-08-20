#custom permission
from rest_framework import permissions
class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # get
            return True
        else: # put, delete, post
            bool(request.user and request.user.is_staff)

class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # get
            return True
        else:
            return obj.user == request.user # je  comment korbe sei sudhu edit korbe
        
        
        
#custom permission  : https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions