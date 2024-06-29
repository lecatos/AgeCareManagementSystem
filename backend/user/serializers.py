from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "first_name": {'required': True, 'allow_blank': False},
            "last_name": {'required': True, 'allow_blank': False},
            "username": {'required': True, 'allow_blank': False},
            "password": {'required': True, 'allow_blank': False, 'write_only': True},
            "sex": {'required': True, 'allow_blank': False},
            "dob": {'required': True}
        }
        #exclude = ["password"]
    def create(self, validated_data):
        print(validated_data)
        #validated_data["username"]=  "asdf"
        validated_data.pop("groups")
        validated_data.pop("user_permissions")
        user = User(**validated_data)
        user.set_password(validated_data.get("password"))
        user.is_active = True
        user.save()
        return user
    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        password = validated_data.get("password")
        if password:
            instance.set_password(validated_data.get("password"))
        instance.save()
        return instance