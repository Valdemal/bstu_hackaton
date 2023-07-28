from user_app.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff',)
        read_only_fields = ('id', 'username', 'email', 'is_staff')
