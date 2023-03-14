from django.db import models

# Create your models here.


class service(models.Model):
    service_name = models.CharField(max_length=255)
    service_about = models.TextField(blank=True)
    service_specialist_photo = models.ImageField(upload_to="photos/specialist/")
    service_create = models.DateTimeField(auto_now_add=True)
    service_update = models.DateTimeField(auto_now=True)
    service_work = models.BooleanField(default=True)
