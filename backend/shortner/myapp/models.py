from django.db import models
from django.contrib.auth.models import User


class ShortURL(models.Model):  
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "short_urls", null = True)
    original_url =  models.URLField()
    short_code = models.CharField(max_length = 10 , unique = True, db_index = True)
    click_count = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    expires_at = models.DateTimeField(null = True , blank = True)

    def __str__(self) : 
        return self.short_code 
    


