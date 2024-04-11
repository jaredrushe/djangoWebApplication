from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models

class Podcast(models.Model):
    pod_name = models.CharField(max_length=200)
    pod_type = models.CharField(max_length=200)
 
    def __str__(self):
        return self.area_name
    
    def get_absolute_url(self):
        return reverse('areadetail', kwargs={'pk':self.pk})