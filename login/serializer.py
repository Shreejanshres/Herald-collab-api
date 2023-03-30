from rest_framework import serializers
from .models import *

class userfarmerserializer(serializers.ModelSerializer):
    class Meta:
        model=user_farmer
        fields='__all__'

class usersellerserializer(serializers.ModelSerializer):
    class Meta:
        model=user_seller
        fields='__all__'

class cropdetailserializer(serializers.ModelSerializer):
    class Meta:
        model=cropdetail
        fields='__all__'