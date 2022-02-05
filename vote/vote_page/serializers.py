from rest_framework import serializers
from .models import Answer, Question, Choice


class ChoiceCreateSerializer(serializers.ModelSerializer):
    """Добавление варианта ответа"""
    class Meta:
        model = Choice
        fields = ['pk', 'question', 'title', 'enabled_choise', ]


class QuestionSerializer(serializers.ModelSerializer):
    """Создания вопроса и вывод списка вопросов"""
    class Meta:
        model = Question
        fields = ['pk', 'title', 'date', 'unvisible']


class ChoiceSerializer(serializers.ModelSerializer):
    """Вывод списка вариантов ответов"""
    question = QuestionSerializer(read_only=True, many=False)

    class Meta:
        model = Choice
        fields = ['pk', 'question', 'title', 'enabled_choise']


class ChoiseDetailSerializer(serializers.ModelSerializer):
    """Редактирование вопроса"""
    class Meta:
        model = Choice
        fields = ['pk', 'question', 'title', 'enabled_choise']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Вывод одного вопроса"""
    choise = ChoiceCreateSerializer(many=True)

    class Meta:
        model = Question
        fields = ['title', 'date', 'choise']


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
