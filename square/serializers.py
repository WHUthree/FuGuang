from django.shortcuts import render

# Create your views here.

from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.response import Response


class recruit_messageSerializer(serializers.ModelSerializer):
    #participants = UserSerializer(many=True)
    #post_user = UserSerializer(many=True)
    class Meta:
        model = MealInfo
        fields = '__all__'


class meal_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealInfo
        exclude = {'end_time','joined_num'}


class LeftMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeftMessage
        fields = '__all__'


class AppraiseSerializer(serializers.ModelSerializer):
    #recipient = UserSerializer()
    class Meta:
        model = Appraise
        fields = "__all__"


class ShareSerializer(serializers.ModelSerializer):
    #post_user = UserSerializer()
    class Meta:
        model = Share
        fields = "__all__"
