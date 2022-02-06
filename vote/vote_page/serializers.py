from rest_framework import serializers
from .models import Answer, Question, Choice


class ChoiceCreateSerializer(serializers.ModelSerializer):
    """Добавление варианта ответа"""
    class Meta:
        model = Choice
        fields = ['pk', 'question', 'title']


class ChoiceSerializer(serializers.ModelSerializer):
    """Вывод всех вариантов ответа"""
    class Meta:
        model = Choice
        fields = ['pk', 'title']


class QuestionSerializer(serializers.ModelSerializer):
    """Создания вопроса и вывод списка вопросов"""

    class Meta:
        model = Question
        fields = ['pk', 'title', 'date', 'unvisible']


class QuestionForChoiceDetailSerializer(serializers.ModelSerializer):
    """Вывод вопросов для вариантов ответа"""
    choice_f = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['title', 'choice_f']


class QuestionDetailSerializer(serializers.ModelSerializer):
    """Вывод одного вопроса"""
    choice_f = ChoiceCreateSerializer(many=True)
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Question
        fields = ['title', 'date', 'choice_f', 'url']


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


class AnswerSerializer(serializers.ModelSerializer):
    """Добавление ответа и вывод результатов"""
    choice = serializers.SlugRelatedField(
        slug_field='title', read_only=True)

    class Meta:
        model = Answer
        fields = ["choice"]


class ChoiceForResultsSerializer(serializers.ModelSerializer):
    """Общее количество вариантов для вопроса и вывод в результатах"""
    count_answer = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['title', 'count_answer']

    def get_count_answer(self, obj):
        return obj.answer_choiсe.count()


class ResultsSerializer(serializers.ModelSerializer):
    """Вывод результатов завершённых опросов"""
    count_choice = serializers.SerializerMethodField()
    choice_f = ChoiceForResultsSerializer(many=True)

    class Meta:
        model = Question
        fields = ['title', 'date', 'choice_f', 'count_choice']

    def get_count_choice(self, obj):
        return obj.choice_f.count()
