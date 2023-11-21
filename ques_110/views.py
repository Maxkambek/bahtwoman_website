from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, UserQuestions
from .serializer import QuestionSerializer, QuestionSerializer2, UserQuestionsSerializer
from rest_framework import generics


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListAPIView2(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer2


class CheckTestAPIView(APIView):
    def post(self, request):
        user = self.request.user.id
        data = self.request.data['results']
        for i in data:
            if i == 'true':
                try:
                    user_qs = UserQuestions.objects.create(
                        user_id=user,
                        question_id=int(i)
                    )
                    user_qs.save()
                except:
                    pass
        return Response('success', status=200)


class UserQuestionsListAPIView(generics.ListAPIView):
    queryset = UserQuestions.objects.all()
    serializer_class = UserQuestionsSerializer
