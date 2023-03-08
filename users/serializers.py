from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Accounts


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = (
            'id', 'username', 'user_type', 'fullname', 'email', 'age', 'gender', 'phone_number', 'bio', 'password')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('user_type', 'username', 'fullname', 'email', 'age', 'gender', 'phone_number', 'bio', 'password')

    def create(self, validated_data):
        user = Accounts.objects.create_user(username=validated_data['username'], user_type=validated_data['user_type'],
                                            email=validated_data['email'],
                                            fullname=validated_data['fullname'],
                                            age=validated_data['age'],
                                            gender=validated_data['gender'],
                                            phone_number=validated_data['phone_number'], bio=validated_data['bio'],
                                            password=validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')
