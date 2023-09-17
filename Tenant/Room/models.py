from django.db import models
from django.utils import timezone

# Create your models here.

class Apartment(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    #bedrooms = models.IntegerField()
    #sqft = models.IntegerField()
    #photo_main = models.URLField()
    #photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self):
        return str(self.title)



