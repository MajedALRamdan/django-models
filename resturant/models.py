from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100,default="")
    opening_time=models.TimeField(default="00:00:00")
    closing_time=models.TimeField(default="00:00:00")
    created_at=models.DateTimeField(auto_now_add=True)
   