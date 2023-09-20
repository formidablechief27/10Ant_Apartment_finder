from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Apartment
from .serializers import ApartmentSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.




class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all().order_by('-list_date')
    #permission_classes = (IsAuthenticated,)
    serializer_class = ApartmentSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

