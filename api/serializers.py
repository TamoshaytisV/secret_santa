from rest_framework import serializers

from core.models import Gift


class GiftSerializer(serializers.ModelSerializer):
    """
    Gift model serializer.
    """
    class Meta:
        model = Gift
        fields = '__all__'
