from rest_framework import serializers
from .models import Service
from django.db import models

class StaffListingField(serializers.RelatedField):
 
     def to_representation(self, value):
         return {"id": value.id,
                 "first_name": value.first_name,
                 "last_name": value.last_name,
                 "username": value.username
                 }
     def to_internal_value(self, value):
         return value

class ClientListingField(serializers.RelatedField):
     def to_representation(self, value):
         return {"id": value.id,
                 "first_name": value.first_name,
                 "last_name": value.last_name,
                 }
     def to_internal_value(self, value):
         return value
     
class ServiceSerializer(serializers.ModelSerializer):
    staff_associated = StaffListingField(many=True, queryset=Service.objects.all())
    client_associated = ClientListingField(many=True, queryset=Service.objects.all())
    class Meta:
        model = Service
        fields = "__all__"
        extra_kwargs = {
            "name": {'required': True},
            "type": {'required': True},
            "location": {'required': True},
            "duration": {'required': True},
            "category": {'required': True},
            "staff_associated": {'required': True},
            "client_associated": {'required': True},
        }
        #exclude = ["staff_associated"]