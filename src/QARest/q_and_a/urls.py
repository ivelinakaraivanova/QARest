from django.urls import path, include
from rest_framework.routers import DefaultRouter

from q_and_a.views import QuestionViewSet, AnswerCreate, AnswerList, AnswerRetrieveUpdateDestroy

router = DefaultRouter()
router.register('questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answer_create/', AnswerCreate.as_view()),
    path('questions/<slug:slug>/answers/', AnswerList.as_view()),
    path('answers/<int:pk>/', AnswerRetrieveUpdateDestroy.as_view()),
]