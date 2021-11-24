from rest_framework import serializers
from .models import CustomUser, UserInfo

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'uid', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'uid', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'], 
            validated_data['email'], 
            validated_data['password'],
        )

        return user

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('uid', 'displayName', 'email', 'profilePic', 'phone', 'gender', 'dateOfBirth',)