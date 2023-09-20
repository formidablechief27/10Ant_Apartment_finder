from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Apartment, CustomUser
from .serializers import ApartmentSerializer, CustomUserSerializer, CustomUserListDetailSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListDetailSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Apartment.objects.all().order_by('-list_date')
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ApartmentSerializer

    def perform_create(self, serializer):
        print("User" + self.request.user.username)
        serializer.save(owner=self.request.user)
        print("end breakpoint")



    

