from rest_framework import serializers
from .models import Client, Allergy, ClientAllergy, ClientMedHist
from django.db import models

class MedHistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientMedHist
        fields = "__all__"
        extra_kwargs = {
            "facility": {'required': True},
            "client": {'required': True},
            "date": {'required': True}
        }

class ClientSerializer(serializers.ModelSerializer):
    allergy = serializers.ReadOnlyField()
    medhist = MedHistSerializer(read_only=True, many=True)

    avatar= serializers.ImageField(
            max_length=None, use_url=True
        )
    class Meta:
        model = Client
        fields = "__all__"
        extra_kwargs = {
            "first_name": {'required': True, 'allow_blank': False},
            "last_name": {'required': True, 'allow_blank': False},
            "sex": {'required': True, 'allow_blank': False},
            "dob": {'required': True}
        }
    
class ClientAllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAllergy
        fields = ["allergy"]

class ClientAllergySerializer2_Backup(serializers.ModelSerializer):
    allergy = serializers.SerializerMethodField()
    class Meta:
        model = ClientAllergy
        fields = ["allergy"]

    def get_allergy(self, obj):
        allergys = Allergy.objects.filter(clientallergy__client=self.context["client"])
        return [allergy.allergy for allergy in allergys]

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = ["allergy"]

class AllergyRequestSerializer(serializers.Serializer):
    allergy = Allergy.allergy

    def create(self, validated_data):
        return Allergy.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.allergy = validated_data.get('allergy', instance.allergy)
        instance.save()
        return instance
