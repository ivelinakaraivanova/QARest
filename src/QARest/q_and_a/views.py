from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from q_and_a.models import Question, Answer
from q_and_a.serializers import QuestionSerializer, AnswerSerializer
from q_and_a.permissions import IsAuthor


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class AnswerCreate(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=slug)
        serializer.save(author=user, question=question)


class AnswerList(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug)


class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
