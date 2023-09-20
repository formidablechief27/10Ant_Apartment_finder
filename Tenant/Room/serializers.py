from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from .models import Apartment, CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class ApartmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Apartment
        lookup_field = "id"
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
                                       username=validated_data['username']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class CustomUserListDetailSerializer(serializers.ModelSerializer):
    apartments = serializers.PrimaryKeyRelatedField(many=True, queryset=Apartment.objects.all())

    class Meta:
        model = CustomUser
        fields = ["id", "email", "username", "apartments"]

