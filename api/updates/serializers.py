from rest_framework import serializers

from updates.models import UpdateSubscription


class UpdateSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateSubscription
        fields = '__all__'
