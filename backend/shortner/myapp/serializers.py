from rest_framework import serializers 
from .models import ShortURL 

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

    