from django.db import models
from rest_framework import serializers
from ..models import Question


class ChoiceSerializer(serializers.Serializer):
    content = serializers.CharField()
    comment = serializers.CharField()
    is_right = serializers.BooleanField()


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"
