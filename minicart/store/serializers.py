from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
import re

class ProductmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
    def validate(self,attrs):
        pr=attrs.get("price")
        nm=attrs.get("name")
        pattern=r'^[A-Za-z ,_-]+$'
        if pr<0:
            raise serializers.ValidationError("Invalid price amount")
        return attrs
    
class UsermodelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self, validated_data):
        # return User.objects.create_user(**validated_data)
        return User.objects.create_superuser(**validated_data)
    