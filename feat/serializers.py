from rest_framework import serializers

from core.models import Feat


class FeatSerializer(serializers.ModelSerializer):
    """Serializer for a feat object"""

    class Meta:
        model = Feat
        fields = ('id', 'text', 'tags')