from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.GetQuestionListView.as_view(), name='questions'),
    path('new_question/', views.NewQuestionListView.as_view(), name='new_question'),
    path("question/<int:pk>/", views.GetQuestionDetailListView.as_view(),
         name='detail_question'),
    path('question/<int:pk>/update_question/', views.UpdateQuestionListView.as_view(),
         name='update_question'),

    path("choiсes/", views.GetChoiseListView.as_view(), name='choiсes'),
    path("create_choiсe/", views.CreateChoiseApiView.as_view(), name='create_choiсe'),
    path("choise/<int:pk>/", views.GetChoiceDetailListView.as_view(),
         name='detail_choiсe'),
    path("choiсe/<int:pk>/update_choiсe", views.UpdateChoiсeListView.as_view(),
         name='update_choiсe'),
    path('question/<int:pk>/answer/',
         views.AddAnswerApiView.as_view(), name='answer'),
    path('results/', views.VotingResultsApiView.as_view(), name='results')
]
