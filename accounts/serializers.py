from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=9
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
       # Cria o user já com senha criptografada
       user = User.objects.create_user(
           username=validated_data['username'],
           email=validated_data['email'],
           password=validated_data['password']
       )
       return user