from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationVariant
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    location_type = LocationSerializer()
    class Meta:
        model = Job
        fields = '__all__'
        #exclude = ['id']
