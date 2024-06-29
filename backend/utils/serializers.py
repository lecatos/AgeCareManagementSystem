from rest_framework import serializers

class LimitOffsetPaginationSerializer(serializers.Serializer):
    offset = serializers.IntegerField(default=0, min_value=0)
    limit = serializers.IntegerField(min_value=1)