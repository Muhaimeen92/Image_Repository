from django.db import models
from django.conf import settings

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to="media/")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    file_name = models.CharField(max_length=64)


