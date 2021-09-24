from rest_framework import serializers

from account.models import CustomUser
from customer.models import Customer


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(username=validated_data['username'], first_name=validated_data['first_name'],
                          last_name=validated_data['last_name'], phone=validated_data['phone'],
                          email=validated_data['email'], )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePassSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}

