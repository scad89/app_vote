import datetime
from random import choice
from urllib import request
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Avg, Count
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .models import Choice, Question, Answer
from .serializers import (
    QuestionSerializer,
    AnswerSerializer,
    QuestionDetailSerializer,
    ChoiceCreateSerializer,
    UpdateDetailQuestionSerializer,
    ChoiceSerializer,
    ResultsSerializer
)


class NewQuestionListView(generics.CreateAPIView):
    """Создание вопроса"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class UpdateQuestionListView(generics.RetrieveUpdateAPIView):
    """Редактирование вопроса"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = UpdateDetailQuestionSerializer


class GetQuestionListView(generics.ListAPIView):
    """Вывод списка вопросов"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.filter(unvisible=False).filter(
        date__gte=datetime.date.today())
    serializer_class = QuestionSerializer


class GetQuestionDetailListView(generics.RetrieveAPIView):
    """Вывод одного вопроса"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    lookup_field = 'pk'


class CreateChoiseApiView(generics.CreateAPIView):
    """Добавление варианта ответа"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Choice.objects.all()
    serializer_class = ChoiceCreateSerializer


class GetChoiseListView(generics.ListAPIView):
    """Вывод списка вариантов ответов"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class GetChoiceDetailListView(generics.RetrieveAPIView):
    """Вывод одного вопроса"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class UpdateChoiсeListView(generics.RetrieveUpdateAPIView):
    """Редактирование варианта ответа"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AddAnswerApiView(generics.ListCreateAPIView):
    """Добавление ответа пользователем"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question = serializer.validated_data.get('question')
        if Answer.objects.filter(question=question).filter(user_id=self.request.user.id).exists():
            raise ValidationError(
                'Вы уже отвечали на этот вопрос.')
        else:
            serializer.save(user_id=self.request.user)

    def get(self, request, pk):
        p = Choice.objects.filter(question_id=pk).all()
        serializer = ChoiceSerializer(p, many=True)
        return Response(serializer.data)


class VotingResultsApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
#    queryset = Answer.objects.all()
#    serializer_class = ResultsSerializer

    def get(self, request):
        question = Question.objects.all()
        print(question)
#        choice = Choice.objects.filter(question=question.)
        serializer = ChoiceSerializer(choice, many=True)
        return Response(serializer.data)
