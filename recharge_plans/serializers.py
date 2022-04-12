from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from .models import Plans


class RechargePlanSerializer(ModelSerializer):

    class Meta:
        model = Plans
        exclude = ['active']