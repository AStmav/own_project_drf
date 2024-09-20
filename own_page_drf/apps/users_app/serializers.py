from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'info')

    def create(self, validate_data):
        user =User(
            username=validate_data['username'],
            info=validate_data.get('info', '')
        )
        user.set_password(validate_data['password'])
        user.save()
        return user