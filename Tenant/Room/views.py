from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Apartment
from .serializers import ApartmentSerializer

# Create your views here.

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all().order_by('-list_date')
    serializer_class = ApartmentSerializer

    

