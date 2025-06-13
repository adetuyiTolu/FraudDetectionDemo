from rest_framework import serializers
from .models import FraudCheckLog


class FraudCheckkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraudCheckLog
        fields = "__all__"
