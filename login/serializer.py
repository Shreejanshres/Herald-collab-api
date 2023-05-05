from rest_framework import serializers
from .models import *

class farmerserializer(serializers.ModelSerializer):
    class Meta:
        model=farmer
        fields='__all__'

class sellerserializer(serializers.ModelSerializer):
    class Meta:
        model=seller
        fields='__all__'

class cropdetailserializer(serializers.ModelSerializer):
    class Meta:
        model=cropdetail
        fields='__all__'
        
class eventserializer(serializers.ModelSerializer):
    class Meta:
        model=event
        fields='__all__'