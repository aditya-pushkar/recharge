from rest_framework.serializers import ModelSerializer

from .models import Recharge


class RechargeSerializer(ModelSerializer):

    class Meta:
        model = Recharge
        fields = '__all__'