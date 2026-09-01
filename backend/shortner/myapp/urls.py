from django.urls import path 
from .views import CreateShortURLView  , URLListView , URLDetailedView


urlpatterns = [
    path('shorten/',CreateShortURLView.as_view(), name = 'create-short-url'),
    path('urls/' , URLListView.as_view() , name = 'urls-list'),
    path('urls/<int:pk>/', URLDetailedView.as_view() , name = 'url-detail'),
]