from rest_framework import serializers
from .models import Inventory, InvHis
from django.db import models

class InvHisSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvHis
        fields = "__all__"

class InventorySerializer(serializers.ModelSerializer):
    weekly_avg = InvHisSerializer(read_only=True, many=True)
    class Meta:
        model = Inventory
        fields = "__all__"
        extra_kwargs = {
            "item_name": {'required': True, 'allow_blank': False},
            "critical_point": {'required': True},
            "qty": {'required': True},
            "desc": {'required': False}
        }