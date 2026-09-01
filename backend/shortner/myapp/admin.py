from django.contrib import admin
from .models import ShortURL 

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_code' , 'original_url' , 'click_count' , 'created_at')
    search_fields = ('short_code' , 'original_url')


