from django.urls import path
from .views import RegisterQuestionVariantCreateAPIView, RegisterQuestionCreateAPIView

urlpatterns = [
    path('question/', RegisterQuestionCreateAPIView.as_view()),
    path('question-variant/', RegisterQuestionVariantCreateAPIView.as_view()),
]
