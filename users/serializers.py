from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
from dj_rest_auth.registration.serializers import RegisterSerializer



class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    image = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['image']
    
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', '')
        } 

# class UserSerializer(serializers.ModelSerializer):
#     days_since_joined = serializers.SerializerMethodField()
#     class Meta:
#         model = Profile
#         fields = ["username","id","days_since_joined"]
#     def get_days_since_joined(self, obj):
#         return (timezone.now() - obj.date_joined).days