from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'password2', 'phone']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        if len(attrs.get('password')) < 8:
            raise serializers.ValidationError({"password": "Пароль должен содержать минимум 8 символов"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)