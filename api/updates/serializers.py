from rest_framework import serializers

from updates.models import UpdateSubscription


class UpdateSubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UpdateSubscription
        fields = '__all__'
