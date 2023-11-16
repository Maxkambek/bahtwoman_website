from .models import Question
from .serializer import QuestionSerializer, QuestionSerializer2
from rest_framework import generics


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListAPIView2(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer2
