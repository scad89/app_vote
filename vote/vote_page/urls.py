from django.urls import path
from . import views


urlpatterns = [
    path('question/', views.GetQuestionListView.as_view(), name='question'),
    path('new_question/', views.NewQuestionListView.as_view(), name='new_question'),
    path('update_question/<int:pk>/', views.UpdateQuestionListView.as_view(),
         name='update_question'),
    path("question/<int:pk>/", views.GetQuestionDetailListView.as_view()),
    path("create_choise/", views.CreateChoiseApiView.as_view(), name='create_choise'),
    path("choise/", views.GetChoiseListView.as_view(), name='choise'),
    path("choise/<int:pk>/", views.UpdateChoiсeListView.as_view(),
         name='update_choise'),
    path('answer', views.AddAnswerApiView.as_view(), name='answer')
]
