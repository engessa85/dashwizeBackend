from rest_framework import serializers
from .models import UserPaymentInfo

class UserPaymentInfoSerailizer(serializers.ModelSerializer):
    class Meta:
        model = UserPaymentInfo
        fields = "__all__"