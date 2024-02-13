from rest_framework import serializers

from ..User.serializers import UserSerializer
from .models import *

class MealInfoSerializer(serializers.ModelSerializer):

    participants = UserSerializer(many=True)

    class Meta:
        model = MealInfo
        fields = "__all__"


class AppraiseSerializer(serializers.ModelSerializer):

    receipient = UserSerializer()

    class Meta:
        model = Appraise
        fields = "__all__"


class ShareInfoSerializer(serializers.ModelSerializer):

    post_user = UserSerializer()

    class Meta:
        model = Share
        fields = "__all__"