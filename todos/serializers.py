from rest_framework import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(required=True, max_length=150)
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'password',
        ]
        
    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email address")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
 