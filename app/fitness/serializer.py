from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'user', 'type', 'start_time', 'stop_time', 'distance', 'calories')
