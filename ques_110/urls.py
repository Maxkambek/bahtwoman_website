from django.urls import path
from .views import QuestionListAPIView, QuestionListAPIView2

urlpatterns = [
    path('for-sidebar/', QuestionListAPIView.as_view()),
    path('by-id/<int:pk>/', QuestionListAPIView2.as_view()),
]
