from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from accounts import models
from accounts.models import Profile


class GuardusRegistrationSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=20)

    def custom_signup(self, request, user):
        user.nickname = self.validated_data.get('nickname', '')
        user.save(update_fields=['nickname'])

class ProfileSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='username.username')
    nickname = serializers.ReadOnlyField(source='username.nickname')
    email = serializers.ReadOnlyField(source='username.email')

    class Meta:
        model=Profile
        fields=['username','nickname','email','address','warning']

class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            'nickname',
            'address',
        )