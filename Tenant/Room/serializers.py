from rest_framework import serializers

from .models import Apartment

class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apartment
        fields = ['title', 'address', 'city', 'price', 'list_date']