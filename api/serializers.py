from rest_framework import serializers

from core.models import Gift


class GiftSerializer(serializers.ModelSerializer):
    """
    Gift model serializer.
    """
    presentee_name = serializers.SerializerMethodField()

    class Meta:
        model = Gift
        fields = '__all__'

    def get_presentee_name(self, obj):
        return obj.presentee.get_full_name() or obj.presentee.username
