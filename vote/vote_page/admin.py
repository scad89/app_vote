from django.contrib import admin
from .models import Question, Answer, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'visible',
    )


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'title',
        'enabled_choise'
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'choice',
        'created',
        'user_id'
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
