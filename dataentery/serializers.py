from rest_framework import serializers
from .models import MtoM, ProfitLoss

class MtoMSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtoM
        fields = "__all__"


class ProfitLossSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfitLoss
        fields = "__all__"