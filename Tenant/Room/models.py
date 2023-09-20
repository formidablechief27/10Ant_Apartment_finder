from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Apartment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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



