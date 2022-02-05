import datetime
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
    ChoiseDetailSerializer
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


class CreateChoiseApiView(generics.CreateAPIView):
    """Добавление варианта ответа"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Choice.objects.all()
    serializer_class = ChoiceCreateSerializer


class GetChoiseListView(generics.ListAPIView):    # вывести сами вопросы а не id
    """Вывод списка вариантов ответов"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class UpdateChoiсeListView(generics.RetrieveUpdateAPIView):
    """Редактирование вопроса"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Choice.objects.all()
    serializer_class = ChoiseDetailSerializer


class AddAnswerApiView(generics.ListCreateAPIView):
    """Добавление ответа пользователем"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get(self, request):
        queryset = Question.objects.all()
        serializer = QuestionDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
