from rest_framework import serializers
from .models import User, Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Blog
        fields = '__all__'
    
    def validated_data(self,value):
        if len(value)<10:
            raise serializer.ValidationError("title is small more then 10 charakter")
        return value