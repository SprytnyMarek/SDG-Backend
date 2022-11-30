from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serlializers import *
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics

# Create your views here.

#-----------------------------------USER VIEW-----------------------------------------------

def say_hello(reqest):
    return HttpResponse('Hello n World')

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Get Users': '/allusers',
        'Add Users': '/user/create',
        'Update Users': '/user/pk/update',
        'Delete Users': '/user/pk/delete',
        'Get Electricty Consumption': '/allelectricty',
        'Add Electricty Consumption': '/electricity/create',
        'Update Electricty Consumption': '/electricity/pk/update',
        'Delete Electricty Consumption': '/electricity/pk/delete',
        'Get Water Consumption': '/allwater',
        'Add Water Consumption': '/water/create',
        'Update Water Consumption': '/water/pk/update',
        'Delete Water Consumption': '/water/pk/delete',
    }
  
    return Response(api_urls)

class UserCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = User.objects.all(),
    serializer_class = UserSerializer

class UserUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def view_users(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        users = User.objects.filter(**request.query_params.dict())
    else:
        users = User.objects.all()
  
    # if there is something in items else raise error
    if users:
        data = UserSerializer(users, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user(request, pk):
    item = get_object_or_404(User, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#-----------------------------------ELECTRICITY VIEW-----------------------------------------------

class ElectricityCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = ElectrictyConsumption.objects.all(),
    serializer_class = ElectricitySerializer

class ElectrictyUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = ElectrictyConsumption.objects.all()
    serializer_class = ElectricitySerializer

class ElectricityDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = ElectrictyConsumption.objects.all()
    serializer_class = ElectricitySerializer

@api_view(['GET'])
def view_electricity_consumption(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        view_electricity_consumption = ElectrictyConsumption.objects.filter(**request.query_params.dict())
    else:
        view_electricity_consumption = ElectrictyConsumption.objects.all()
  
    # if there is something in items else raise error
    if view_electricity_consumption:
        data = ElectricitySerializer(view_electricity_consumption, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        view_electricity_consumption = ElectrictyConsumption.objects.filter(**request.query_params.dict())
    else:
        view_electricity_consumption = ElectrictyConsumption.objects.all()
  
    # if there is something in items else raise error
    if view_electricity_consumption:
        data = ElectricitySerializer(view_electricity_consumption, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------WATER VIEW-----------------------------------------------

class WaterCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = WaterConsumption.objects.all(),
    serializer_class = WaterSerializer

class WaterUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = WaterConsumption.objects.all()
    serializer_class = WaterSerializer

class WaterDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = WaterConsumption.objects.all()
    serializer_class = WaterSerializer

@api_view(['GET'])
def view_water_consumption(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        waters = WaterConsumption.objects.filter(**request.query_params.dict())
    else:
        waters = WaterConsumption.objects.all()
  
    # if there is something in items else raise error
    if waters:
        data = WaterSerializer(waters, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------HEATING VIEW-----------------------------------------------

class HeatingCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = HeatingConsumption.objects.all(),
    serializer_class = HeatingSerializer

class HeatingUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = HeatingConsumption.objects.all()
    serializer_class = HeatingSerializer

class HeatingDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = HeatingConsumption.objects.all()
    serializer_class = HeatingSerializer

@api_view(['GET'])
def view_heating_consumption(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        heatings = HeatingConsumption.objects.filter(**request.query_params.dict())
    else:
        heatings = HeatingConsumption.objects.all()
  
    # if there is something in items else raise error
    if heatings:
        data = HeatingSerializer(heatings, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------LEAGUE VIEW-----------------------------------------------

class LeagueCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = League.objects.all(),
    serializer_class = LeagueSerializer

class LeagueUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class LeagueDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

@api_view(['GET'])
def view_league(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        leagues = League.objects.filter(**request.query_params.dict())
    else:
        leagues = League.objects.all()
  
    # if there is something in items else raise error
    if leagues:
        data = LeagueSerializer(leagues, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------QUIZ VIEW-----------------------------------------------

class QuizCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Quiz.objects.all(),
    serializer_class = QuizSerializer

class QuizUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

@api_view(['GET'])
def view_quiz(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        quizez = Quiz.objects.filter(**request.query_params.dict())
    else:
        quizez = Quiz.objects.all()
  
    # if there is something in items else raise error
    if quizez:
        data = QuizSerializer(quizez, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------QUIZ QUESTION VIEW-----------------------------------------------

class QuizQuestionCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Quiz_question.objects.all(),
    serializer_class = QuizQuestionSerializer

class QuizQuestionUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Quiz_question.objects.all()
    serializer_class = QuizQuestionSerializer

class QuizQuestionDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Quiz_question.objects.all()
    serializer_class = QuizQuestionSerializer

@api_view(['GET'])
def view_quiz_question(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        quizez_questions = Quiz_question.objects.filter(**request.query_params.dict())
    else:
        quizez_questions = Quiz_question.objects.all()
  
    # if there is something in items else raise error
    if quizez_questions:
        data = QuizQuestionSerializer(quizez_questions, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------QUIZ ANSWER VIEW-----------------------------------------------

class QuizAnswerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Quiz_answer.objects.all(),
    serializer_class = QuizAnswerSerializer

class QuizAnswerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Quiz_answer.objects.all()
    serializer_class = QuizAnswerSerializer

class QuizAnswerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Quiz_answer.objects.all()
    serializer_class = QuizAnswerSerializer

@api_view(['GET'])
def view_quiz_answer(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        quizez_answer = Quiz_answer.objects.filter(**request.query_params.dict())
    else:
        quizez_answer = Quiz_answer.objects.all()
  
    # if there is something in items else raise error
    if quizez_answer:
        data = QuizAnswerSerializer(quizez_answer, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#-----------------------------------TAKE VIEW-----------------------------------------------

class TakeCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Take.objects.all(),
    serializer_class = TakeSerializer

class TakeUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Take.objects.all()
    serializer_class = TakeSerializer

class TakeDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Take.objects.all()
    serializer_class = TakeSerializer

@api_view(['GET'])
def view_take(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        takes = Take.objects.filter(**request.query_params.dict())
    else:
        takes = Take.objects.all()
  
    # if there is something in items else raise error
    if takes:
        data = TakeSerializer(takes, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#-----------------------------------TAKE ANSWER VIEW-----------------------------------------------

class TakeAnswerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Take_answer.objects.all(),
    serializer_class = TakeAnswerSerializer

class TakeAnswerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Take_answer.objects.all()
    serializer_class = TakeAnswerSerializer

class TakeAnswerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Take_answer.objects.all()
    serializer_class = TakeAnswerSerializer

@api_view(['GET'])
def view_take_answer(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        takeanswers = Take_answer.objects.filter(**request.query_params.dict())
    else:
        takeanswers = Take_answer.objects.all()
  
    # if there is something in items else raise error
    if takeanswers:
        data = TakeAnswerSerializer(takeanswers, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)