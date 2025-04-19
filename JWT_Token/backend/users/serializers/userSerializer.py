
from rest_framework import serializers
from ..models import User

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'name', 'email', 'password', 'is_active', 'is_staff']
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, user, validated_data):
        password = validated_data.pop('password', None)
        for key, value in validated_data.items():
            setattr(user, key, value)

        if password:
            user.set_password(password)

        user.save()
        return user
    

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'name', 'email', 'is_active', 'image']