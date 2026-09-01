from django.urls import path 
from .views import CreateShortURLView  , RedirectURLView

urlpatterns = [
    path('shorten/',CreateShortURLView.as_view(), name = 'create-shprt-url'),
    
]