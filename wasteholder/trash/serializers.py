
from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import *

class Collectorserializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class Houseserializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = '__all__'
        