from django.shortcuts import get_object_or_404 , redirect 
from rest_framework.views import APIView 
from rest_framework.response import  Response
from rest_framework import status 

from .models import ShortURL 
from .serializers  import ShortURLSerializer 
from .utils import generate_short_code 

class CreateShortURLView(APIView) : 
    def post(self, request)  : 
        serializer = ShortURLSerializer(data = request.data)
        if not serializer.is_valid(): 
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        short_code  = generate_short_code()

        while ShortURL.objects.filter(short_code = short_code).exists() : 
            short_code = generate_short_code()

        url = serializer.save(short_code = short_code)

        return Response({
            "id" : url.id , 
            "original_url" : url.original_url , 
            "short_code " :  url.short_code , 
            'short_url'  : (f'http://127.0.0.1:8000/'
                            f'{url.short_code}/'
            ),
            
        },
        status = status.HTTP_201_CREATED)


class RedirectURLView(APIView) : 
    def get(self, request , short_code)  :
        url = get_object_or_404(ShortURL, short_code = short_code)
        url.click_count += 1 
        url.save(update_fields = ['click_count'])
        return redirect(url.original_url) 

        
    
        
         
        
        
