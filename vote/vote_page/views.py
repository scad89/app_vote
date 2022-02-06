import datetime
from django.forms import ValidationError
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
    ResultsSerializer,
    QuestionForChoiceDetailSerializer
)


class NewQuestionListView(generics.CreateAPIView):
    """Создание вопроса"""
    permission_classes = [permissions.IsAuthenticated]
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
    queryset = Question.objects.filter(
        unvisible=False
    ).filter(
        date__gte=datetime.date.today()
    )
    serializer_class = QuestionSerializer


class GetQuestionDetailListView(generics.RetrieveAPIView):
    """Вывод одного вопроса"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.filter(
        unvisible=False
    ).filter(
        date__gte=datetime.date.today()
    )
    serializer_class = QuestionDetailSerializer
    lookup_field = 'pk'


class CreateChoiceApiView(generics.CreateAPIView):
    """Добавление варианта ответа"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceCreateSerializer


class GetChoiceListView(generics.ListAPIView):
    """Вывод списка вариантов ответов"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.filter(
        unvisible=False
    ).filter(
        date__gte=datetime.date.today()
    )
    serializer_class = QuestionForChoiceDetailSerializer


class GetChoiceDetailListView(generics.RetrieveAPIView):
    """Вывод одного вопроса"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class UpdateChoiceListView(generics.RetrieveUpdateAPIView):
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
        if Answer.objects.filter(
            question=question
        ).filter(
            user_id=self.request.user.id
        ).exists():
            raise ValidationError(
                'Вы уже отвечали на этот вопрос.')
        else:
            serializer.save(user_id=self.request.user)

    def get(self, request, pk):
        p = Choice.objects.filter(question_id=pk).all()
        serializer = ChoiceSerializer(p, many=True)
        return Response(serializer.data)


class VotingResultsApiView(generics.ListAPIView):
    """Вывод результатов"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.filter(
        unvisible=False
    ).filter(
        date__lte=datetime.date.today()
    ).prefetch_related(
        'choice_f', 'answer_question'
    )
    serializer_class = ResultsSerializer
