from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    password_2 = serializers.CharField(
        write_only = True,
        required = True
    )
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=models.CustomUser.objects.all())]
    )
    class Meta:
        model = models.CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_2']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_2')

        user = models.CustomUser.objects.create_user(
            username = validated_data['username'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', ''),
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user