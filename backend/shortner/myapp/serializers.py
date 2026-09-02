from rest_framework import serializers 
from .models import ShortURL 
from django.contrib.auth.models import User 


class ShortURLSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model  = ShortURL 
        fields = [
            'id', 
            'original_url',
            'short_code', 
            'click_count' , 
            'created_at' , 
            'expires_at'
        ]
        read_only_fields = [
            'id',
            'short_code' , 
            'click_count' ,
            'created_at',
            'expires_at'
        ]

class RegisterSerializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only = True , min_length = 8)
    class Meta : 
        model = User 
        fields = [
            'username' , 
            'email', 
            'password'
        ]
    def create(self, validated_data) :
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'] , 
            password = validated_data['password']
        )

        return user