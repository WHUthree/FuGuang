from django.shortcuts import render

# Create your views here.

from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.response import Response


class recruit_messageSerializer(serializers.ModelSerializer):
    #participants = UserSerializer(many=True)
    #post_user = UserSerializer(many=True)
    grade = serializers.MultipleChoiceField(choices=MealInfo.grade_choice)
    class Meta:
        model = MealInfo
        exclude = ['participants','is_complete']
        extra_kwargs = {
            'post_user': {'read_only': True}
        }

    def validate(self, data):
        if data['end_time'] > data['meal_time']:
            raise serializers.ValidationError("meal_time should not be earlier than end_time")
        return data


class meal_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealInfo
        exclude = ['grade','end_time','joined_num','is_complete']


class LeftMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeftMessage
        fields = "__all__"
        extra_kwargs = {
            'sender': {'read_only': True}
        }


class AppraiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraise
        fields = "__all__"


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = "__all__"
        extra_kwargs = {
            'post_user': {'read_only': True},
            'likes': {'read_only': True},
            'post_time': {'read_only': True}
        }
