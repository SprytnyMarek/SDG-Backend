from django.db.models import fields
from rest_framework import serializers
from .models import *
  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'email', 'username', 'friends']

class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectrictyConsumption
        fields = '__all__'

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterConsumption
        fields = ['waterSourceName', 'waterConsumptionPerHour', 'unit', 'hoursOfUsage', 'user']

class HeatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatingConsumption
        fields = '__all__'

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_question
        fields = '__all__'

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_question
        fields = '__all__'

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz_answer
        fields = '__all__'

class TakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Take
        fields = '__all__'

class TakeAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Take_answer
        fields = '__all__'