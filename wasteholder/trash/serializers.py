
from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'


        
class Collectorserializer(serializers.ModelSerializer):
    user = Userserializer(read_only=True)
    area = AreaSerializer(read_only=True)
    class Meta:
        model = Collector
        fields = ('__all__')

class Houseserializer(serializers.ModelSerializer):
    
    # area = AreaSerializer(read_only=True)
    class Meta:
        model = Houses
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    collector = Collectorserializer(read_only=True)
    houses = Houseserializer(read_only=True)
    class Meta:
        model = ActivityLog
        fields = '__all__'

        