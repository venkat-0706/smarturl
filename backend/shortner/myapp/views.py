from django.shortcuts import get_object_or_404 , redirect 
from rest_framework.views import APIView 
from rest_framework.response import  Response
from rest_framework import status 
from django.utils import timezone 
from datetime import timedelta
from rest_framework.permissions import AllowAny
from myapp.serializers import RegisterSerializer


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

        expires_at = timezone.now() + timedelta(hours = 24)

        url = serializer.save(short_code = short_code ,expires_at = expires_at)


        return Response({
            "id" : url.id , 
            "original_url" : url.original_url , 
            "short_code" :  url.short_code , 
            'short_url'  : (f'http://127.0.0.1:8000/'
                            f'{url.short_code}/'
            ),
            "expires_at" : url.expires_at,
            
        },
        status = status.HTTP_201_CREATED)


class RedirectURLView(APIView) : 
    def get(self, request , short_code)  :
        url = get_object_or_404(ShortURL, short_code = short_code)

        if url.expires_at <= timezone.now() : 
            return Response({
                "error" : "This short URL has been expired.."
            }, status =  status.HTTP_410_GONE)
        
        url.click_count += 1 
        url.save(update_fields = ['click_count'])
        return redirect(url.original_url) 

class URLListView(APIView) : 
    def get(self, request) : 
        urls = ShortURL.objects.all().order_by('-created_at')
        serializer = ShortURLSerializer(urls , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)

class URLDetailedView(APIView) : 
    def get(self, request, pk) :
        url = get_object_or_404(ShortURL , id = pk)
        serializer = ShortURLSerializer(url) 
        return Response(serializer.data , status = status.HTTP_200_OK)

    def delete(self, request, pk) : 
        url =  get_object_or_404(ShortURL , id = pk) 
        url.delete()
        return Response({
            "message" : "ShortURL deleted successfully"
        } , status = status.HTTP_204_NO_CONTENT)
    
class RegisterView(APIView) :
    permission_classes = [AllowAny] 
    def post(self, request) : 
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message"  : "User Registered Successfully...",
                "username" :  user.username
            }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    



    
        
         
        
        
