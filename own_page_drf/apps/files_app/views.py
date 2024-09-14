from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer
from django.contrib.auth.models import Group

from rest_framework.permissions import BasePermission

class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        """
        Takes a user and a group name, and returns `True` if the user is in that group.
        """
        try:
            return Group.objects.get(name='subscribers').user_set.filter(id=request.user.id).exists()
        except Group.DoesNotExist:
            return False
class FileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsSubscriber]

# Create your views here.
