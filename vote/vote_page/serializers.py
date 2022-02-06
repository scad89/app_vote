from rest_framework import serializers
from .models import Answer, Question, Choice
from django.db.models import Avg, Count


class ChoiceCreateSerializer(serializers.ModelSerializer):
    """Добавление варианта ответа"""
    class Meta:
        model = Choice
        fields = ['pk', 'question', 'title']


class QuestionSerializer(serializers.ModelSerializer):
    """Создания вопроса и вывод списка вопросов"""
    class Meta:
        model = Question
        fields = ['pk', 'title', 'date', 'unvisible']


class ChoiceSerializer(serializers.ModelSerializer):
    """Вывод списка вариантов ответов"""
    question = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Choice
        fields = ['pk', 'question', 'title']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Вывод одного вопроса"""
    choiсe = ChoiceCreateSerializer(many=True)

    class Meta:
        model = Question
        fields = ['title', 'date', 'choiсe']


class UpdateDetailQuestionSerializer(serializers.ModelSerializer):
    """Редактирование вопроса"""
    class Meta:
        model = Question
        fields = ['title', 'date', 'unvisible']


class AnswerSerializer(serializers.ModelSerializer):
    """Добавление ответа пользователем"""
    class Meta:
        model = Answer
        fields = ['question', 'choice']


class ResultsSerializer(serializers.ModelSerializer):
    """Вывод результатов"""
    class Meta:
        model = Answer
        fields = ['question', 'choice']
